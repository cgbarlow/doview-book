#!/usr/bin/env python3
"""Generate a README.md inside each Part folder under docs/md/.

Each Part README lists its chapters in numerical order with links to the
chapter's xxquestion.md as the entry point.
"""

import re
from pathlib import Path

MD_DIR = Path('/workspaces/workspace-basic/doview-book/docs/md')

PART_DESCRIPTIONS = {
    'A': "The five generic steps of DoView Planning and how to apply them within standard government, corporate, and nonprofit planning, implementation, and reporting cycles.",
    'B': "How DoView strategy/outcomes diagrams work: drawing rules, conventions, drill-down structure, multi-stakeholder coordination, and 'what-if' planning.",
    'C': "Setting priorities and aligning activities, projects, and outputs against outcomes using DoView Visual Alignment.",
    'D': "The DoView Planning Framework, indicator/output/KPI selection, and good-indicator checklists.",
    'E': "Contracting and delegating for outcomes versus outputs, social investment, social bonds, and PPP suitability.",
    'F': "Using DoView for performance improvement, benchmarking, league-tabling, and embedding evidence in strategy diagrams.",
    'G': "Types of evaluation, strategic evaluation/research planning, impact evaluation suitability, economic evaluation, and M&E plans.",
    'H': "Reporting indicators and evaluation results back against a DoView strategy, complementing Balanced Scorecards, RBA, and Investment Logic Maps.",
    'I': "Introducing DoView Planning into organisations, putting diagrams into existing planning documents, workflow changes, and meeting-room setup.",
    'J': "Applying outcomes theory and DoView Planning to AI agents, prompting, communication mapping, mathematisation, and dialog processes.",
}


def numeric_key(folder_name: str) -> tuple:
    """Sort key extracting the numeric chapter ordinal.

    A1 -> (1, '')   A5 -> (5, '')
    G2 -> (2, '')   G2A -> (2, 'A')   G10 -> (10, '')
    """
    # Folder name starts with "XX - …" where XX is e.g. "A1", "G2A", "B25"
    code = folder_name.split(' - ')[0]
    m = re.match(r'^[A-Z]+(\d+)([A-Z]*)$', code)
    if not m:
        return (999, code)
    return (int(m.group(1)), m.group(2))


def part_letter(part_folder_name: str) -> str:
    # "Part A - DoView Planning Fundamentals" -> "A"
    m = re.match(r'^Part ([A-Z]) - ', part_folder_name)
    return m.group(1) if m else '?'


def part_title(part_folder_name: str) -> str:
    # "Part A - DoView Planning Fundamentals" -> "DoView Planning Fundamentals"
    return part_folder_name.split(' - ', 1)[1] if ' - ' in part_folder_name else part_folder_name


def chapter_link_text(folder_name: str) -> str:
    """Convert 'A1 - The Five Steps...' to 'A1 — The Five Steps...' (em dash)."""
    if ' - ' in folder_name:
        code, _, title = folder_name.partition(' - ')
        return f"{code} — {title}"
    return folder_name


def chapter_code(folder_name: str) -> str:
    """Extract the lowercase chapter code, e.g. 'A1' -> 'a1', 'G2A' -> 'g2a'."""
    code = folder_name.split(' - ')[0]
    return code.lower()


def generate_for_part(part_dir: Path) -> str:
    letter = part_letter(part_dir.name)
    title = part_title(part_dir.name)
    description = PART_DESCRIPTIONS.get(letter, "")

    chapter_folders = sorted(
        [d for d in part_dir.iterdir() if d.is_dir()],
        key=lambda d: numeric_key(d.name),
    )

    lines = [
        "---",
        f"part: {letter}",
        f"title: {title}",
        "kind: part-index",
        f"chapters: {len(chapter_folders)}",
        "---",
        "",
        f"# Part {letter} — {title}",
        "",
        description,
        "",
        "## Chapters",
        "",
    ]
    for ch in chapter_folders:
        text = chapter_link_text(ch.name)
        # Link to the question.md inside the chapter folder (entry point)
        code = chapter_code(ch.name)
        link = f"<{ch.name}/{code}question.md>"
        lines.append(f"- [{text}]({link})")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("[← Back to book front page](../../README.md)")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    part_dirs = sorted(
        [d for d in MD_DIR.iterdir() if d.is_dir() and d.name.startswith('Part ')],
        key=lambda d: d.name,
    )
    for pd in part_dirs:
        # index.md (not README.md) so GitHub Pages serves it as the folder index
        # without needing a Jekyll plugin. GitHub.com's web UI also auto-renders
        # index.md as the folder view, so the editorial experience is the same.
        index = pd / 'index.md'
        index.write_text(generate_for_part(pd))
        print(f"Wrote {index.relative_to(MD_DIR)}")


if __name__ == '__main__':
    main()
