"""Tests for the link rewriter (ADR-013).

Pure function tests — no I/O, no HTTP. The rewriter takes a markdown
string, the source file's relative path (so it can resolve relative
links), a mapping of `relative_path → diagram_id`, and the
introduction id for back-link fallback. It returns the rewritten
markdown.
"""

from __future__ import annotations

from pathlib import PurePosixPath

import pytest

from link_rewriter import strip_frontmatter, rewrite_links


# ---------------------------------------------------------------------------
# strip_frontmatter
# ---------------------------------------------------------------------------

class TestStripFrontmatter:
    def test_strips_yaml_frontmatter_at_top(self) -> None:
        content = "---\nkind: tool\npair: a01\n---\n\n# Title\n\nBody."
        body, fm = strip_frontmatter(content)
        assert body == "# Title\n\nBody."
        assert fm == {"kind": "tool", "pair": "a01"}

    def test_returns_input_unchanged_when_no_frontmatter(self) -> None:
        content = "# Title\n\nBody without frontmatter."
        body, fm = strip_frontmatter(content)
        assert body == content
        assert fm == {}

    def test_leaves_horizontal_rules_in_body_alone(self) -> None:
        # A document body containing `---` lines (e.g. before a footer)
        # must not be confused with frontmatter delimiters.
        content = "# Title\n\nBody.\n\n---\n\nFooter."
        body, fm = strip_frontmatter(content)
        assert body == content
        assert fm == {}


# ---------------------------------------------------------------------------
# rewrite_links — set-up helpers
# ---------------------------------------------------------------------------

# Simulate a 3-file corpus:
#   /1 - introduction.md                                            → intro_id
#   /Part A - Foo/index.md                                          → part_a_id
#   /Part A - Foo/A01 - The Steps/a01question.md                    → q_id
#   /Part A - Foo/A01 - The Steps/a01tool.md                        → t_id

INTRO_ID = "00000000-0000-0000-0000-000000000001"
PART_A_ID = "00000000-0000-0000-0000-0000000000a0"
Q_ID = "00000000-0000-0000-0000-0000000000a1"
T_ID = "00000000-0000-0000-0000-0000000000a2"

MAPPING = {
    PurePosixPath("1 - introduction.md"): INTRO_ID,
    PurePosixPath("Part A - Foo/index.md"): PART_A_ID,
    PurePosixPath("Part A - Foo/A01 - The Steps/a01question.md"): Q_ID,
    PurePosixPath("Part A - Foo/A01 - The Steps/a01tool.md"): T_ID,
}


# ---------------------------------------------------------------------------
# rewrite_links — happy paths
# ---------------------------------------------------------------------------

class TestRewriteLinks:
    def test_same_directory_relative_md_link(self) -> None:
        src = PurePosixPath("Part A - Foo/A01 - The Steps/a01question.md")
        content = "Pair: [Tool](a01tool.md)"
        out, unknown = rewrite_links(content, src, MAPPING, INTRO_ID)
        assert out == f"Pair: [Tool](iris://diagram/{T_ID})"
        assert unknown == []

    def test_angle_bracket_link_with_spaces(self) -> None:
        src = PurePosixPath("Part A - Foo/index.md")
        content = "- [A01](<A01 - The Steps/a01question.md>)"
        out, _ = rewrite_links(content, src, MAPPING, INTRO_ID)
        assert out == f"- [A01](iris://diagram/{Q_ID})"

    def test_folder_only_link_resolves_to_index_md(self) -> None:
        # Mirrors the introduction's `[Part A](<Part A - DoView Planning Fundamentals>)`
        src = PurePosixPath("1 - introduction.md")
        content = "- [Part A](<Part A - Foo>)"
        out, _ = rewrite_links(content, src, MAPPING, INTRO_ID)
        assert out == f"- [Part A](iris://diagram/{PART_A_ID})"

    def test_back_link_to_unimported_book_root_readme_routes_to_introduction(self) -> None:
        # The corpus's Part index files have `[← Back](../../README.md)`
        # which points at /doview-book/README.md — outside the import.
        src = PurePosixPath("Part A - Foo/index.md")
        content = "[← Back to book front page](../../README.md)"
        out, _ = rewrite_links(content, src, MAPPING, INTRO_ID)
        assert out == f"[← Back to book front page](iris://diagram/{INTRO_ID})"

    def test_relative_path_to_root_conclusion(self) -> None:
        # Introduction's `[Conclusion](<2 - conclusion.md>)` when conclusion
        # is in the mapping at root.
        mapping = {
            **MAPPING,
            PurePosixPath("2 - conclusion.md"): "conclusion-id",
        }
        src = PurePosixPath("1 - introduction.md")
        content = "- [Conclusion](<2 - conclusion.md>)"
        out, _ = rewrite_links(content, src, mapping, INTRO_ID)
        assert out == "- [Conclusion](iris://diagram/conclusion-id)"


# ---------------------------------------------------------------------------
# rewrite_links — untouched
# ---------------------------------------------------------------------------

class TestRewriteLinksUntouched:
    def test_external_https_link_untouched(self) -> None:
        src = PurePosixPath("1 - introduction.md")
        content = "[author](https://aishock.substack.com/p/authorship-declaration)"
        out, unknown = rewrite_links(content, src, MAPPING, INTRO_ID)
        assert out == content
        assert unknown == []

    def test_mailto_link_untouched(self) -> None:
        src = PurePosixPath("1 - introduction.md")
        content = "[email](mailto:a@b.com)"
        out, _ = rewrite_links(content, src, MAPPING, INTRO_ID)
        assert out == content

    def test_existing_iris_link_untouched(self) -> None:
        src = PurePosixPath("1 - introduction.md")
        content = "[diagram](iris://diagram/abc)"
        out, _ = rewrite_links(content, src, MAPPING, INTRO_ID)
        assert out == content

    def test_same_doc_anchor_link_untouched(self) -> None:
        src = PurePosixPath("1 - introduction.md")
        content = "[heading](#section)"
        out, _ = rewrite_links(content, src, MAPPING, INTRO_ID)
        assert out == content


# ---------------------------------------------------------------------------
# rewrite_links — code-fence awareness
# ---------------------------------------------------------------------------

class TestRewriteLinksRespectsCodeFences:
    def test_links_inside_fenced_code_block_left_alone(self) -> None:
        src = PurePosixPath("Part A - Foo/A01 - The Steps/a01question.md")
        content = (
            "Pair: [Tool](a01tool.md)\n"
            "\n"
            "```\n"
            "[Tool](a01tool.md)\n"
            "```\n"
        )
        out, _ = rewrite_links(content, src, MAPPING, INTRO_ID)
        # First (outside fence) is rewritten; second (inside fence) is not.
        assert out.count(f"iris://diagram/{T_ID}") == 1
        assert "[Tool](a01tool.md)" in out  # the fenced one survives

    def test_mermaid_arrow_inside_block_not_mis_matched(self) -> None:
        # Mermaid flowcharts contain `A-->B` and `[Label]` syntax which
        # look like markdown link parts. They must not be touched.
        src = PurePosixPath("Part A - Foo/A01 - The Steps/a01tool.md")
        content = (
            "# Title\n"
            "\n"
            "```mermaid\n"
            "flowchart TD\n"
            "    A[Client]-->B[Server]\n"
            "    B-->C[(DB)]\n"
            "```\n"
            "\n"
            "Pair: [Question](a01question.md)\n"
        )
        out, _ = rewrite_links(content, src, MAPPING, INTRO_ID)
        # Mermaid block byte-identical.
        assert "A[Client]-->B[Server]" in out
        assert "B-->C[(DB)]" in out
        # The outside-fence link is rewritten.
        assert f"[Question](iris://diagram/{Q_ID})" in out

    def test_inline_code_link_left_alone(self) -> None:
        src = PurePosixPath("1 - introduction.md")
        content = "Use the syntax `[label](target.md)` to link."
        out, _ = rewrite_links(content, src, MAPPING, INTRO_ID)
        assert out == content


# ---------------------------------------------------------------------------
# rewrite_links — unknown links
# ---------------------------------------------------------------------------

class TestRewriteLinksUnknown:
    def test_unknown_relative_link_left_in_place_and_reported(self) -> None:
        src = PurePosixPath("Part A - Foo/A01 - The Steps/a01question.md")
        content = "[missing](nope.md)"
        out, unknown = rewrite_links(content, src, MAPPING, INTRO_ID)
        assert out == content
        assert unknown == ["nope.md"]

    def test_multiple_unknown_links_all_reported(self) -> None:
        src = PurePosixPath("Part A - Foo/A01 - The Steps/a01question.md")
        content = "[a](missing-1.md) and [b](missing-2.md)"
        out, unknown = rewrite_links(content, src, MAPPING, INTRO_ID)
        assert out == content
        assert sorted(unknown) == ["missing-1.md", "missing-2.md"]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
