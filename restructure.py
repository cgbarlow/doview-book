#!/usr/bin/env python3
"""Restructure docs/md into Part folders with chapter subfolders.

Reads the H1 from each *tool.md to derive the chapter title, then moves
the question/tool pair into:
    docs/md/Part X - <part title>/<XX> - <chapter title>/{xxquestion.md,xxtool.md}
"""

import re
import shutil
from pathlib import Path

PARTS = {
    'a': 'DoView Planning Fundamentals',
    'b': 'DoView Drawing and Strategy Principles',
    'c': 'Alignment and Prioritization',
    'd': 'Indicators and Frameworks',
    'e': 'Contracting and Delegation',
    'f': 'Performance Improvement',
    'g': 'Evaluation and Research',
    'h': 'Reporting',
    'i': 'Implementation and Integration',
    'j': 'AI Applications',
}

MD_DIR = Path('/workspaces/workspace-basic/doview-book/docs/md')

CHAPTER_PATTERN = re.compile(r'^([a-z]+\d+[a-z]?)tool\.md$')
TITLE_STRIP = re.compile(r'^DoView Tool [A-Za-z0-9]+\s*[—–\-]\s*(.+)$')


def sanitize_for_path(name: str) -> str:
    # Replace filesystem-unsafe characters with safe ones
    return (name
            .replace('/', ' or ')
            .replace(':', ' -')
            .replace('?', '')
            .replace('"', "'")
            .replace('\\', '-')
            .replace('|', '-')
            .replace('*', '-')
            .replace('<', '')
            .replace('>', '')
            .strip())


def extract_title(tool_md: Path) -> str:
    text = tool_md.read_text()
    # Strip frontmatter
    if text.startswith('---'):
        end = text.find('\n---', 3)
        if end != -1:
            text = text[end + 4:]
    text = text.lstrip()
    # First line should be the H1
    first_line = text.split('\n', 1)[0].lstrip('#').strip()
    m = TITLE_STRIP.match(first_line)
    return (m.group(1) if m else first_line).strip()


def main():
    moved = 0
    skipped = 0
    failed = []

    for tool_md in sorted(MD_DIR.glob('*tool.md')):
        m = CHAPTER_PATTERN.match(tool_md.name)
        if not m:
            failed.append((tool_md.name, 'filename does not match pattern'))
            continue
        code = m.group(1)            # e.g. 'a1', 'g2a'
        letter = code[0]
        if letter not in PARTS:
            failed.append((tool_md.name, f'unknown part letter: {letter}'))
            continue

        title = sanitize_for_path(extract_title(tool_md))
        part_folder = MD_DIR / sanitize_for_path(f'Part {letter.upper()} - {PARTS[letter]}')
        chapter_folder = part_folder / sanitize_for_path(f'{code.upper()} - {title}')

        chapter_folder.mkdir(parents=True, exist_ok=True)

        question_md = MD_DIR / f'{code}question.md'
        if question_md.exists():
            shutil.move(str(question_md), str(chapter_folder / question_md.name))
        else:
            skipped += 1  # missing partner — note but proceed
        shutil.move(str(tool_md), str(chapter_folder / tool_md.name))
        moved += 1
        print(f'{code:6} -> {chapter_folder.relative_to(MD_DIR)}')

    print()
    print(f'Chapters moved: {moved}')
    print(f'Missing question partner: {skipped}')
    if failed:
        print('Failed:')
        for name, reason in failed:
            print(f'  {name}: {reason}')


if __name__ == '__main__':
    main()
