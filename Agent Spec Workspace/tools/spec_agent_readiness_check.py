#!/usr/bin/env python3
"""Validate the NVMe SPEC markdown layer for Codex agent lookup readiness.

This is a structural and routing gate. It does not prove source fidelity by
itself, but it catches issues that commonly break downstream agent use:
missing entry files, broken local references, malformed tables, mojibake, and
incomplete command-folder skeletons.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable
from urllib.parse import unquote


ROOT_REQUIRED_FILES = [
    "SPEC_AGENTS.md",
    "SPEC_REFERENCE_GUIDE.md",
    "Base_Spec_2_0_Index.md",
    "Admin_Command_Spec_Table.md",
    "IO_Command_Spec_Table.md",
    "Status_Code_Reference.md",
    "Command_Status_Matrix.md",
]

MCTP_REQUIRED_FILES = [
    "mctp-base-1.3.1/README.md",
    "mctp-base-1.3.1/MCTP_BASE_INDEX.md",
    "mctp-base-1.3.1/MCTP_COMMON_HEADER_REFERENCE.md",
    "mctp-base-1.3.1/MCTP_CONTROL_COMMAND_REFERENCE.md",
    "mctp-base-1.3.1/MCTP_TO_NVME_MI_BOUNDARY.md",
    "mctp-pcie-vdm-1.0.1/README.md",
    "mctp-pcie-vdm-1.0.1/MCTP_PCIE_VDM_INDEX.md",
    "mctp-pcie-vdm-1.0.1/MCTP_PCIE_VDM_PACKET_REFERENCE.md",
    "mctp-smbus-i2c-1.1.0/README.md",
    "mctp-smbus-i2c-1.1.0/MCTP_SMBUS_I2C_INDEX.md",
    "mctp-smbus-i2c-1.1.0/MCTP_SMBUS_I2C_PACKET_REFERENCE.md",
    "mctp-smbus-i2c-1.1.0/MCTP_SMBUS_I2C_TIMING_ADDRESS_REFERENCE.md",
]

SOURCE_REQUIRED_FILES = [
    "../NVMe Base Spec/2.0/NVMe/NVM-Express-Base-Specification-2_0-2021.06.02-Ratified-5.md",
    "../NVMe Base Spec/2.0/NVMe/NVM-Express-NVM-Command-Set-Specification-2021.06.02-Ratified-1.md",
    "../NVMe Base Spec/2.0/NVMe/NVM-Express-Key-Value-Command-Set-Specification-1.0-2021.06.02-Ratified-1.md",
    "../NVMe Base Spec/2.0/NVMe/NVM-Express-Zoned-Namespace-Command-Set-Specification-1.1-2021.06.02-Ratified-1.md",
    "../NVMe Base Spec/2.0/NVMe/NVM-Express-Management-Interface-1.2-2021.06.02-Ratified.md",
    "../NVMe Base Spec/2.0/NVMe/NVMe-over-PCIe-Transport-Specification-1_0-2021.06.02-Ratified-1.md",
    "../NVMe Base Spec/2.0/NVMe/NVM-Express-RDMA-Transport-Specification-2021.06.02-Ratified-1.md",
    "../NVMe Base Spec/2.0/NVMe/NVM-Express-TCP-Transport-Specification-2021.06.02-Ratified-1.md",
    "../NVMe Base Spec/2.0/MCTP/MCTP-Base-Specification.md",
    "../NVMe Base Spec/2.0/MCTP/MCTP-PCIe-VDM-Transport-Binding-Specification.md",
    "../NVMe Base Spec/2.0/MCTP/MCTP-SMBusI2C-Transport-Binding-Specification.md",
]

LAYER_REQUIRED_FILES = [
    "controller-properties-2.0/README.md",
    "controller-properties-2.0/CONTROLLER_PROPERTY_INDEX.md",
    "controller-properties-2.0/CORE_CONTROLLER_PROPERTIES.md",
    "controller-properties-2.0/ADMIN_QUEUE_INTERRUPT_PROPERTIES.md",
    "controller-properties-2.0/MEMORY_REGION_PROPERTIES.md",
    "controller-properties-2.0/cross-spec-boundary.md",
    "controller-properties-2.0/COMMAND_CONTENT_AUDIT.md",
    "io-command-sets-2.0/README.md",
    "io-command-sets-2.0/COMMAND_SET_AGENTS.md",
    "io-command-sets-2.0/COMMAND_SET_INDEX.md",
    "io-command-sets-2.0/BASE_TO_COMMAND_SET_BOUNDARY.md",
    "io-command-sets-2.0/NVM_COMMAND_SET_INDEX.md",
    "io-command-sets-2.0/KEY_VALUE_COMMAND_SET_INDEX.md",
    "io-command-sets-2.0/ZNS_COMMAND_SET_INDEX.md",
    "fabrics-base-2.0/README.md",
    "fabrics-base-2.0/FABRICS_AGENTS.md",
    "fabrics-base-2.0/FABRICS_COMMAND_SET_INDEX.md",
    "fabrics-base-2.0/BASE_TO_FABRICS_BOUNDARY.md",
    "zns-command-set-1.1/README.md",
    "zns-command-set-1.1/ZNS_COMMAND_SET_INDEX.md",
    "mi-1.2/README.md",
    "mi-1.2/MI_AGENTS.md",
    "mi-1.2/MI_COMMAND_SET_INDEX.md",
    "mi-1.2/MI_COMMAND_REFERENCE.md",
    "mi-1.2/MI_MESSAGE_HEADER_REFERENCE.md",
    "mi-1.2/MI_INBAND_OUTOFBAND_BOUNDARY.md",
    "mi-1.2/admin-through-mi/MI_ADMIN_THROUGH_COMMAND_TABLE.md",
    "mi-1.2/admin-through-mi/field-reference.md",
    "mi-1.2/admin-through-mi/cross-spec-boundary.md",
    "mi-1.2/pcie-through-mi/MI_PCIE_THROUGH_COMMAND_TABLE.md",
    "mi-1.2/pcie-through-mi/field-reference.md",
    "mi-1.2/pcie-through-mi/cross-spec-boundary.md",
    "pcie-transport-1.0/README.md",
    "pcie-transport-1.0/PCIE_TRANSPORT_AGENTS.md",
    "pcie-transport-1.0/PCIE_TRANSPORT_INDEX.md",
    "pcie-transport-1.0/PCIE_REGISTER_FIELD_REFERENCE.md",
    "pcie-transport-1.0/PCIE_TRANSPORT_BEHAVIOR_REFERENCE.md",
    "rdma-transport-1.0/README.md",
    "rdma-transport-1.0/RDMA_TRANSPORT_AGENTS.md",
    "rdma-transport-1.0/RDMA_TRANSPORT_INDEX.md",
    "tcp-transport-1.0/README.md",
    "tcp-transport-1.0/TCP_TRANSPORT_AGENTS.md",
    "tcp-transport-1.0/TCP_TRANSPORT_INDEX.md",
]

COMMAND_REQUIRED_FILES = [
    "README.md",
    "command-facts.md",
    "field-reference.md",
    "status-reference.md",
    "cross-spec-boundary.md",
]

AUDIT_FILE = "COMMAND_CONTENT_AUDIT.md"

SOURCE_TREE_PART = "NVMe Base Spec"
MOJIBAKE_RE = re.compile(r"�|Ã.|ã€|ï¼|å[\x80-\xbf]|æ[\x80-\xbf]|ç[\x80-\xbf]|è[\x80-\xbf]|é[\x80-\xbf]")
MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*]\(([^)]+)\)")
INLINE_PATH_RE = re.compile(r"`([^`\n]*(?:\.md|\.pdf)[^`\n]*)`", re.IGNORECASE)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
ROOT_KNOWN_FILES = set(ROOT_REQUIRED_FILES)


@dataclass
class Finding:
    severity: str
    check: str
    file: str
    line: int | None
    message: str


def rel(path: Path, root: Path) -> str:
    return str(path.relative_to(root)).replace("\\", "/")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig", errors="replace")


def add(
    findings: list[Finding],
    severity: str,
    check: str,
    file: Path | str,
    root: Path,
    message: str,
    line: int | None = None,
) -> None:
    file_text = rel(file, root) if isinstance(file, Path) else file
    findings.append(Finding(severity, check, file_text, line, message))


def is_source_file(path: Path, root: Path) -> bool:
    try:
        return SOURCE_TREE_PART in path.relative_to(root).parts
    except ValueError:
        return False


def slugify_heading(heading: str) -> str:
    heading = re.sub(r"`([^`]*)`", r"\1", heading)
    heading = re.sub(r"<[^>]+>", "", heading)
    heading = re.sub(r"[^\w\u4e00-\u9fff -]", "", heading, flags=re.UNICODE)
    heading = heading.strip().lower().replace(" ", "-")
    heading = re.sub(r"-+", "-", heading)
    return heading


def headings_for(text: str) -> set[str]:
    slugs: set[str] = set()
    counts: dict[str, int] = {}
    for line in text.splitlines():
        match = HEADING_RE.match(line)
        if not match:
            continue
        slug = slugify_heading(match.group(2))
        if not slug:
            continue
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        slugs.add(slug if count == 0 else f"{slug}-{count}")
    return slugs


def normalize_ref(raw: str) -> str | None:
    ref = raw.strip().strip("<>")
    if not ref or ref.startswith(("#", "http://", "https://", "mailto:")):
        return None
    ref = ref.replace("\\", "/")
    if "*" in ref:
        # Glob-like examples are routing instructions, not concrete references.
        return None
    if "/" not in ref and ref not in ROOT_KNOWN_FILES:
        # Inline generic filenames such as `command-facts.md` describe a file
        # model; they are not concrete links from the current directory.
        return None
    if " " in ref and not re.search(r"\.(md|pdf)(#.*)?$", ref, re.IGNORECASE):
        # Likely prose in backticks, not a file reference.
        return None
    return unquote(ref)


def resolve_ref(base_file: Path, root: Path, ref: str) -> tuple[Path, str | None]:
    target, _, anchor = ref.partition("#")
    target = target.replace("\\", "/")
    base = root if target.startswith("/") else base_file.parent
    resolved = (base / target.lstrip("/")).resolve()
    return resolved, anchor or None


def candidate_ref_paths(base_file: Path, root: Path, ref: str) -> tuple[list[Path], str | None]:
    resolved, anchor = resolve_ref(base_file, root, ref)
    candidates = [resolved]
    target, _, _anchor = ref.partition("#")
    target = target.replace("\\", "/").lstrip("/")
    if not Path(target).is_absolute():
        candidates.append((root / target).resolve())
    return candidates, anchor


def iter_markdown_files(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob("*.md") if p.is_file())


def iter_command_dirs(root: Path) -> Iterable[Path]:
    roots = [
        root / "admin-commands-2.0",
        root / "io-commands-2.0",
        root / "fabrics-base-2.0" / "commands",
        root / "io-command-sets-2.0" / "nvm-command-set-1.0" / "admin-commands",
        root / "io-command-sets-2.0" / "nvm-command-set-1.0" / "io-commands",
        root / "io-command-sets-2.0" / "key-value-command-set-1.0" / "io-commands",
        root / "zns-command-set-1.1" / "commands",
        root / "zns-command-set-1.1" / "modified-nvm-commands",
    ]
    for command_root in roots:
        if not command_root.exists():
            continue
        for child in sorted(command_root.iterdir()):
            if child.is_dir():
                yield child


def check_required_files(root: Path, findings: list[Finding]) -> None:
    for name in ROOT_REQUIRED_FILES + MCTP_REQUIRED_FILES + LAYER_REQUIRED_FILES + SOURCE_REQUIRED_FILES:
        path = root / name
        if not path.is_file():
            add(findings, "ERROR", "required-file", name, root, "Required agent lookup file is missing.")


def check_command_dirs(root: Path, findings: list[Finding]) -> None:
    for directory in iter_command_dirs(root):
        for name in COMMAND_REQUIRED_FILES:
            if not (directory / name).is_file():
                add(findings, "ERROR", "command-folder", directory, root, f"Missing required command file: {name}.")
        if not (directory / AUDIT_FILE).is_file():
            add(findings, "WARN", "command-folder", directory, root, f"Missing audit evidence file: {AUDIT_FILE}.")


def check_encoding_and_empty(root: Path, md_files: list[Path], findings: list[Finding]) -> None:
    for path in md_files:
        text = read_text(path)
        if not text.strip():
            add(findings, "ERROR", "empty-file", path, root, "Markdown file is empty.")
            continue
        if is_source_file(path, root):
            continue
        for number, line in enumerate(text.splitlines(), 1):
            if MOJIBAKE_RE.search(line):
                add(findings, "WARN", "mojibake", path, root, "Line contains likely mojibake / replacement text.", number)


def check_tables(root: Path, md_files: list[Path], findings: list[Finding]) -> None:
    for path in md_files:
        if is_source_file(path, root):
            continue
        lines = read_text(path).splitlines()
        for idx, line in enumerate(lines):
            if "|" not in line:
                continue
            if idx + 1 >= len(lines):
                continue
            sep = lines[idx + 1]
            if not re.match(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$", sep):
                continue
            expected = count_table_cells(line)
            if expected < 2:
                continue
            row = idx + 2
            while row < len(lines) and "|" in lines[row].strip():
                cells = count_table_cells(lines[row])
                if cells != expected:
                    add(
                        findings,
                        "ERROR",
                        "markdown-table",
                        path,
                        root,
                        f"Table row has {cells} cells; header has {expected}.",
                        row + 1,
                    )
                row += 1


def count_table_cells(line: str) -> int:
    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]
    return len(stripped.split("|"))


def check_references(root: Path, md_files: list[Path], findings: list[Finding]) -> None:
    heading_cache: dict[Path, set[str]] = {}
    for path in md_files:
        if is_source_file(path, root):
            continue
        text = read_text(path)
        for number, line in enumerate(text.splitlines(), 1):
            raw_refs = [m.group(1) for m in MARKDOWN_LINK_RE.finditer(line)]
            raw_refs.extend(m.group(1) for m in INLINE_PATH_RE.finditer(line))
            for raw_ref in raw_refs:
                ref = normalize_ref(raw_ref)
                if not ref:
                    continue
                candidates, anchor = candidate_ref_paths(path, root, ref)
                existing = next((candidate for candidate in candidates if candidate.exists()), None)
                if existing is None:
                    add(findings, "ERROR", "local-reference", path, root, f"Broken local reference: {raw_ref}", number)
                    continue
                if anchor and existing.suffix.lower() == ".md":
                    headings = heading_cache.get(existing)
                    if headings is None:
                        headings = headings_for(read_text(existing))
                        heading_cache[existing] = headings
                    if anchor.lower() not in headings:
                        add(
                            findings,
                            "WARN",
                            "local-reference",
                            path,
                            root,
                            f"Anchor not found in target: {raw_ref}",
                            number,
                        )


def check_agent_contracts(root: Path, findings: list[Finding]) -> None:
    contracts = {
        "SPEC_AGENTS.md": [
            "Token-Efficient Reading Protocol",
            "For MCTP / NVMe-MI transport substrate lookup",
            "Not explicitly found in the local NVMe Base Specification 2.0 source.",
            "mctp-base-1.3.1\\MCTP_COMMON_HEADER_REFERENCE.md",
            "MCTP_SMBUS_I2C_PACKET_REFERENCE.md",
        ],
        "mctp-base-1.3.1/MCTP_TO_NVME_MI_BOUNDARY.md": [
            "Do not treat MCTP Control commands as NVMe-MI commands.",
            "Do not derive NVMe-MI command payload fields from MCTP packet fields.",
        ],
    }
    for relative, required_strings in contracts.items():
        path = root / relative
        if not path.is_file():
            continue
        text = read_text(path)
        for needle in required_strings:
            if needle not in text:
                add(findings, "ERROR", "agent-contract", path, root, f"Missing required agent contract text: {needle!r}")


def summarize(findings: list[Finding], md_files: list[Path]) -> dict[str, object]:
    errors = [f for f in findings if f.severity == "ERROR"]
    warnings = [f for f in findings if f.severity == "WARN"]
    checks: dict[str, int] = {}
    for finding in findings:
        checks[finding.check] = checks.get(finding.check, 0) + 1
    return {
        "markdown_files": len(md_files),
        "errors": len(errors),
        "warnings": len(warnings),
        "finding_counts_by_check": checks,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate NVMe SPEC markdown agent-readiness.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text.")
    args = parser.parse_args()

    root = args.root.resolve()
    findings: list[Finding] = []
    md_files = iter_markdown_files(root)

    check_required_files(root, findings)
    check_command_dirs(root, findings)
    check_encoding_and_empty(root, md_files, findings)
    check_tables(root, md_files, findings)
    check_references(root, md_files, findings)
    check_agent_contracts(root, findings)

    result = {"summary": summarize(findings, md_files), "findings": [asdict(f) for f in findings]}

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        summary = result["summary"]
        print("NVMe SPEC agent-readiness check")
        print(f"Root: {root}")
        print(f"Markdown files: {summary['markdown_files']}")
        print(f"Errors: {summary['errors']}")
        print(f"Warnings: {summary['warnings']}")
        for finding in findings[:200]:
            location = finding.file if finding.line is None else f"{finding.file}:{finding.line}"
            print(f"{finding.severity} [{finding.check}] {location} - {finding.message}")
        if len(findings) > 200:
            print(f"... {len(findings) - 200} more findings omitted; rerun with --json for full output.")

    return 1 if result["summary"]["errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
