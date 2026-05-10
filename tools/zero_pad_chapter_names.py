#!/usr/bin/env python3
"""Zero-pad chapter folder + file names to Xnn format.

Folder name pattern before: "A1 - Title", "B25 - Title", "G2A - Title"
Folder name pattern after:  "A01 - Title", "B25 - Title", "G02A - Title"

File name pattern before: "a1question.md", "g2aquestion.md"
File name pattern after:  "a01question.md", "g02aquestion.md"

Also rewrites cross-link references inside each chapter file and the
YAML frontmatter `pair:` field. Updates the 10 Part-folder READMEs.

Does NOT touch docs/pdf/* (source PDFs keep their as-published names —
the 1:1 mapping with docs/md/ filenames is superseded; see ADR-012).
"""

import re
from pathlib import Path

MD_DIR = Path('/workspaces/workspace-basic/doview-book/docs/md')

CODE_RE = re.compile(r'^([A-Z]+)(\d+)([A-Z]*)$')


def pad_code(code: str) -> str:
    """A1 -> A01; B25 -> B25; G2A -> G02A; B10 -> B10."""
    m = CODE_RE.match(code)
    if not m:
        return code
    letters, digits, suffix = m.group(1), m.group(2), m.group(3)
    return f"{letters}{int(digits):02d}{suffix}"


def rewrite_links_in_text(text: str, old_code_lc: str, new_code_lc: str) -> str:
    """Replace bare cross-links like `[Tool](a1tool.md)` with the new code.

    Only replaces exact word-boundary matches against the lowercased codes
    inside parentheses (to avoid touching prose mentioning the code).
    Also updates the YAML `pair:` field.
    """
    # File link references: (a1question.md), (a1tool.md)
    text = re.sub(
        rf'\b{re.escape(old_code_lc)}(question|tool)\.md\b',
        rf'{new_code_lc}\1.md',
        text,
    )
    # YAML frontmatter pair field: pair: a1  -> pair: a01
    text = re.sub(
        rf'^(pair:\s*){re.escape(old_code_lc)}\s*$',
        rf'\g<1>{new_code_lc}',
        text,
        flags=re.MULTILINE,
    )
    return text


def process_part_folder(part_dir: Path):
    moves = []  # (old_chapter_dir, new_chapter_dir, old_code_lc, new_code_lc)

    for ch_dir in sorted(part_dir.iterdir()):
        if not ch_dir.is_dir():
            continue
        # Folder name: "XX - Title"
        if ' - ' not in ch_dir.name:
            continue
        old_code, sep, title = ch_dir.name.partition(' - ')
        new_code = pad_code(old_code)
        new_folder_name = f"{new_code} - {title}"
        new_dir = part_dir / new_folder_name
        old_code_lc = old_code.lower()
        new_code_lc = new_code.lower()
        moves.append((ch_dir, new_dir, old_code_lc, new_code_lc))

    # Phase 1: rename files inside each chapter folder (in place), rewrite content
    for ch_dir, new_dir, old_lc, new_lc in moves:
        if old_lc == new_lc and ch_dir == new_dir:
            continue
        for f in list(ch_dir.iterdir()):
            if f.is_file() and f.name.endswith('.md'):
                # Rewrite content first
                content = f.read_text()
                content = rewrite_links_in_text(content, old_lc, new_lc)
                f.write_text(content)
                # Then rename the file if the code changed
                if old_lc != new_lc:
                    new_name = f.name.replace(f"{old_lc}question", f"{new_lc}question") \
                                     .replace(f"{old_lc}tool", f"{new_lc}tool")
                    if new_name != f.name:
                        new_path = f.with_name(new_name)
                        f.rename(new_path)

    # Phase 2: rename chapter folders
    for ch_dir, new_dir, old_lc, new_lc in moves:
        if ch_dir != new_dir:
            ch_dir.rename(new_dir)
            print(f"  {ch_dir.name}  ->  {new_dir.name}")


def main():
    for part_dir in sorted(MD_DIR.iterdir()):
        if part_dir.is_dir() and part_dir.name.startswith('Part '):
            print(f"=== {part_dir.name} ===")
            process_part_folder(part_dir)
    print("\nRegenerating Part-folder READMEs to pick up new names…")


if __name__ == '__main__':
    main()
