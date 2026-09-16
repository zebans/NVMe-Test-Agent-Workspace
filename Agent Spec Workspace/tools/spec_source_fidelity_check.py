#!/usr/bin/env python3
"""Check command source anchors against the converted authoritative sources.

This gate verifies ownership, declared section existence, figure placement, and
folder/opcode consistency. It complements, but does not replace, semantic field
and behavior review against the original specification.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Finding:
    severity: str
    file: str
    message: str


def source_for(path: Path, root: Path) -> Path | None:
    rel = path.relative_to(root).as_posix()
    source_root = root.parent / "NVMe Base Spec" / "2.0" / "NVMe"
    if rel.startswith(("admin-commands-2.0/", "io-commands-2.0/", "fabrics-base-2.0/")):
        return source_root / "NVM-Express-Base-Specification-2_0-2021.06.02-Ratified-5.md"
    if rel.startswith("io-command-sets-2.0/nvm-command-set-1.0/"):
        return source_root / "NVM-Express-NVM-Command-Set-Specification-2021.06.02-Ratified-1.md"
    if rel.startswith("io-command-sets-2.0/key-value-command-set-1.0/"):
        return source_root / "NVM-Express-Key-Value-Command-Set-Specification-1.0-2021.06.02-Ratified-1.md"
    if rel.startswith("zns-command-set-1.1/"):
        return source_root / "NVM-Express-Zoned-Namespace-Command-Set-Specification-1.1-2021.06.02-Ratified-1.md"
    return None


def declared_source(text: str) -> str | None:
    for line in text.splitlines()[:20]:
        if re.search(r"(?i)(?:primary\s+)?source", line):
            return line
    return None


def explicit_source_lines(text: str) -> list[str]:
    return [
        line
        for line in text.splitlines()
        if re.match(r"(?i)^\s*(?:(?:primary\s+)?source\s*:|\|\s*(?:primary\s+)?source\s*\|)", line)
    ]


def section_region(source: str, section: str) -> str | None:
    heading_pattern = re.compile(rf"(?m)^{re.escape(section)}[ \t]+(?![^\n]*\.{{3,}})[^\n]+$")
    headings = list(heading_pattern.finditer(source))
    if not headings:
        return None
    heading = headings[-1]
    parts = section.split(".")
    sibling = re.compile(
        rf"(?m)^{re.escape('.'.join(parts[:-1]))}\.\d+[ \t]+(?![^\n]*\.{{3,}})[^\n]+$"
        if len(parts) > 1
        else rf"(?m)^\d+[ \t]+(?![^\n]*\.{{3,}})[^\n]+$"
    )
    next_heading = sibling.search(source, heading.end())
    return source[heading.start() : next_heading.start() if next_heading else len(source)]


def figure_numbers(source_line: str) -> set[int]:
    figures: set[int] = set()
    for match in re.finditer(r"(?i)Figures?\s+(\d+)(?:\s*(?:-|through|to)\s*(\d+))?", source_line):
        start = int(match.group(1))
        end = int(match.group(2) or start)
        figures.update(range(start, end + 1))
    return figures


def command_name(text: str) -> str | None:
    match = re.search(r"\|\s*(?:Command|Base command)\s*\|\s*([^|]+?)\s*\|", text)
    return match.group(1).strip().strip("`") if match else None


def source_has_inferred_section(source: str, section: str, command: str | None) -> bool:
    child = re.search(rf"(?m)^{re.escape(section)}\.\d+[ \t]+[^\n]+$", source)
    if not child or not command:
        return False
    normalized = re.sub(r"^(?:NVM|ZNS-Modified)\s+", "", command, flags=re.IGNORECASE)
    return bool(re.search(rf"(?i)\b{re.escape(normalized)}\s+command\b", source))


def is_global_opcode_figure(owner: Path, figure: int) -> bool:
    expected = {
        "NVM-Express-Base-Specification-2_0-2021.06.02-Ratified-5.md": {138, 375, 390},
        "NVM-Express-NVM-Command-Set-Specification-2021.06.02-Ratified-1.md": {18},
        "NVM-Express-Key-Value-Command-Set-Specification-1.0-2021.06.02-Ratified-1.md": {5},
        "NVM-Express-Zoned-Namespace-Command-Set-Specification-1.1-2021.06.02-Ratified-1.md": {12},
    }
    return figure in expected.get(owner.name, set())


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate SPEC command source anchors.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    findings: list[Finding] = []
    checked = 0
    anchors_checked = 0
    source_cache: dict[Path, str] = {}

    for markdown in sorted(root.rglob("*.md")):
        owner = source_for(markdown, root)
        if owner is None:
            continue
        source = source_cache.setdefault(owner, owner.read_text(encoding="utf-8-sig", errors="replace"))
        rel = markdown.relative_to(root).as_posix()
        for line in explicit_source_lines(markdown.read_text(encoding="utf-8-sig")):
            anchors_checked += 1
            section_match = re.search(r"(?i)section\s+([0-9]+(?:\.[0-9]+)*)", line)
            if section_match:
                section = section_match.group(1)
                if section_region(source, section) is None and not re.search(
                    rf"(?m)^{re.escape(section)}\.\d+[ \t]+[^\n]+$", source
                ):
                    findings.append(Finding("ERROR", rel, f"Source line names section {section}, which is absent from the owner source."))
            for figure in sorted(figure_numbers(line)):
                if not re.search(rf"Figure\s+{figure}\b", source, re.IGNORECASE):
                    findings.append(Finding("ERROR", rel, f"Source line names Figure {figure}, which is absent from the owner source."))

    for facts in sorted(root.rglob("command-facts.md")):
        owner = source_for(facts, root)
        if owner is None:
            continue
        checked += 1
        rel = facts.relative_to(root).as_posix()
        text = facts.read_text(encoding="utf-8-sig")
        line = declared_source(text)
        if line is None:
            findings.append(Finding("ERROR", rel, "No source declaration in the first 20 lines."))
            continue

        source = source_cache.setdefault(owner, owner.read_text(encoding="utf-8-sig", errors="replace"))
        command = command_name(text)
        section_match = re.search(r"(?i)section\s+([0-9]+(?:\.[0-9]+)*)", line)
        if section_match:
            section = section_match.group(1)
            region = section_region(source, section)
            if region is None:
                if not source_has_inferred_section(source, section, command):
                    findings.append(Finding("ERROR", rel, f"Declared section {section} was not found in {owner.name}."))
                for figure in sorted(figure_numbers(line)):
                    if not re.search(rf"Figure\s+{figure}\b", source, re.IGNORECASE):
                        findings.append(Finding("ERROR", rel, f"Declared Figure {figure} does not exist in the owner source."))
            else:
                heading = region.splitlines()[0]
                if command and command.lower() not in heading.lower():
                    findings.append(
                        Finding(
                            "ERROR",
                            rel,
                            f"Section {section} heading is {heading!r}, not the declared {command} command.",
                        )
                    )
                for figure in sorted(figure_numbers(line)):
                    if re.search(rf"Figure\s+{figure}\b", region, re.IGNORECASE):
                        continue
                    if not re.search(rf"Figure\s+{figure}\b", source, re.IGNORECASE):
                        findings.append(Finding("ERROR", rel, f"Declared Figure {figure} does not exist in the owner source."))
                        continue
                    if is_global_opcode_figure(owner, figure):
                        continue
                    findings.append(
                        Finding("WARN", rel, f"Declared Figure {figure} exists, but is outside section {section}; review cross-reference intent.")
                    )

        folder_match = re.match(r"([0-9a-fA-F]{2})h-", facts.parent.name)
        opcode_match = re.search(r"\|\s*(?:Admin opcode|I/O opcode|Opcode)\s*\|\s*`([0-9a-fA-F]{2})h`", text)
        if folder_match and opcode_match and folder_match.group(1).lower() != opcode_match.group(1).lower():
            findings.append(
                Finding(
                    "ERROR",
                    rel,
                    f"Folder opcode {folder_match.group(1)}h disagrees with declared opcode {opcode_match.group(1)}h.",
                )
            )

    print("NVMe SPEC source-fidelity anchor check")
    print(f"Root: {root}")
    print(f"Command facts checked: {checked}")
    print(f"Explicit source lines checked: {anchors_checked}")
    errors = sum(f.severity == "ERROR" for f in findings)
    warnings = sum(f.severity == "WARN" for f in findings)
    print(f"Errors: {errors}")
    print(f"Warnings: {warnings}")
    for finding in findings:
        print(f"{finding.severity} {finding.file} - {finding.message}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
