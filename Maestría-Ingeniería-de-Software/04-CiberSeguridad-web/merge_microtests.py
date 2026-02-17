#!/usr/bin/env python3
"""Merge MicroTest sections from Markdown files into a single file.

Usage:
    python merge_microtests.py --root . --output microtests_unificados.md --sort --dedupe
"""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys

# Match H1-H3 headings that contain any MicroTest variation (case-insensitive).
MICROTEST_HEADER_RE = re.compile(
    r"^(#{1,3})\s+.*\bmicro\s*-?\s*test\b.*$",
    re.IGNORECASE,
)

# Match files with a 3-digit numeric prefix like 001-... up to 051-....
FILE_PREFIX_RE = re.compile(r"^(\d{3})-.*\.md$", re.IGNORECASE)


def is_microtest_header(line: str) -> tuple[bool, int]:
    # Detect MicroTest header and capture its heading level.
    match = MICROTEST_HEADER_RE.match(line.strip())
    if not match:
        # No MicroTest header on this line.
        return False, 0
    # Return True and the header level count (#, ##, ###).
    return True, len(match.group(1))


def is_same_level_header(line: str, level: int) -> bool:
    # Build a regex that matches headers of the same level.
    pattern = rf"^#{'{' + str(level) + '}'}\s+"
    # Return True when the current line is a same-level header.
    return re.match(pattern, line.strip()) is not None


def extract_microtests(text: str) -> list[str]:
    # Split content into lines while keeping line endings.
    lines = text.splitlines(keepends=True)
    # Collect each extracted MicroTest section.
    results: list[str] = []

    # Track current position and capture state.
    i = 0
    in_capture = False
    current: list[str] = []
    level = 0

    # Scan line-by-line to locate and capture MicroTest sections.
    while i < len(lines):
        line = lines[i]
        if not in_capture:
            # Start capturing when a MicroTest header is found.
            is_header, level = is_microtest_header(line)
            if is_header:
                in_capture = True
                current = [line]
            i += 1
            continue

        # Stop capture when a same-level header is found.
        if is_same_level_header(line, level):
            results.append("".join(current))
            in_capture = False
            current = []
            # Re-evaluate this line for a new MicroTest header.
            continue

        # Keep collecting lines inside the MicroTest section.
        current.append(line)
        i += 1

    # Append any trailing MicroTest section that reaches EOF.
    if in_capture and current:
        results.append("".join(current))

    # Return all captured MicroTest sections.
    return results


def is_target_file(path: Path) -> bool:
    # Enforce the 001-051 file range by name prefix.
    match = FILE_PREFIX_RE.match(path.name)
    if not match:
        return False

    # Parse the numeric prefix and check the range.
    number = int(match.group(1))
    if number < 1 or number > 51:
        return False

    # Ignore summary files when the name contains "resumen".
    if "resumen" in path.name.lower():
        return False

    # Only accept files that meet all filters.
    return True


def main() -> int:
    # Define CLI arguments for root folder and output settings.
    parser = argparse.ArgumentParser(description="Merge MicroTest sections from Markdown files.")
    parser.add_argument("--root", default=".", help="Root folder to scan (recursive).")
    parser.add_argument(
        "--output",
        default="microtests_unificados.md",
        help="Output Markdown file path.",
    )
    parser.add_argument("--sort", action="store_true", help="Sort by filename.")
    parser.add_argument("--dedupe", action="store_true", help="Avoid duplicate MicroTests.")

    # Parse CLI arguments.
    args = parser.parse_args()

    # Resolve the root folder and output file location.
    root = Path(args.root).resolve()
    output_path = Path(args.output)
    if not output_path.is_absolute():
        output_path = root / output_path

    # Validate the root folder before scanning.
    if not root.exists() or not root.is_dir():
        print(f"Root folder not found: {root}", file=sys.stderr)
        return 1

    # Gather candidate Markdown files with the 001-051 prefix rule.
    md_files = [
        p
        for p in root.rglob("*.md")
        if is_target_file(p) and p.resolve() != output_path.resolve()
    ]

    # Accumulate all MicroTest sections found across files.
    microtests: list[tuple[Path, int, str]] = []
    for md_file in md_files:
        try:
            # Read the file contents as UTF-8.
            text = md_file.read_text(encoding="utf-8")
        except Exception as exc:
            # Skip unreadable files but report the issue.
            print(f"Warning: could not read {md_file}: {exc}", file=sys.stderr)
            continue

        # Warn on empty files to surface missing content.
        if text.strip() == "":
            print(f"Warning: empty file {md_file}", file=sys.stderr)
            continue

        # Extract all MicroTest sections for this file.
        for idx, mt in enumerate(extract_microtests(text)):
            # Inject source filename after the MicroTest header line.
            lines = mt.splitlines(keepends=True)
            if lines:
                lines.insert(1, f"**Archivo:** {md_file.name}\n\n")
            microtests.append((md_file, idx, "".join(lines)))

    # Optionally sort by file name and occurrence index.
    if args.sort:
        microtests.sort(key=lambda item: (str(item[0]).lower(), item[1]))

    # Optionally de-duplicate identical MicroTest content.
    seen: set[str] = set()
    merged: list[str] = []
    for _path, _idx, content in microtests:
        normalized = content.strip()
        if args.dedupe:
            if normalized in seen:
                continue
            seen.add(normalized)
        merged.append(normalized + "\n")

    # Merge sections with a Markdown divider between each MicroTest.
    divider = "\n---\n\n"
    output_text = divider.join(merged)
    output_path.write_text(output_text, encoding="utf-8")

    # Print a summary for quick verification.
    print(f"MicroTests encontrados: {len(merged)}")
    print(f"Archivo generado: {output_path}")
    return 0


if __name__ == "__main__":
    # Execute the main function when the script is run directly.
    raise SystemExit(main())
