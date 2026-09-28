"""Unit tests for src/log_helper.py."""

from __future__ import annotations

from pathlib import Path

import pytest

from src.log_helper import report_group, report_notice, write_step_summary


def test_report_notice_is_noop_locally(
    capfd: pytest.CaptureFixture[str],
) -> None:
    """Outside CI nothing should be printed; callers emit their own output."""
    with pytest.MonkeyPatch().context() as mp:
        mp.delenv("GITHUB_ACTIONS", raising=False)
        report_notice("Done. 3 new article(s) written.")
        captured = capfd.readouterr()
        assert captured.out == ""
        assert captured.err == ""


@pytest.mark.parametrize(
    ("env_value", "expected_line"),
    [
        ("true", "::notice::Done. 3 new article(s) written."),
        ("True", ""),
        ("", ""),
    ],
)
def test_report_notice_ci_flag(
    capfd: pytest.CaptureFixture[str],
    monkeypatch: pytest.MonkeyPatch,
    env_value: str,
    expected_line: str,
) -> None:
    monkeypatch.setenv("GITHUB_ACTIONS", env_value)
    report_notice("Done. 3 new article(s) written.")
    captured = capfd.readouterr()
    if expected_line:
        assert captured.out == expected_line + "\n"
    else:
        assert captured.out == ""


def test_report_notice_with_title(
    capfd: pytest.CaptureFixture[str],
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("GITHUB_ACTIONS", "true")
    report_notice("Done. 3 new article(s) written.", title="Scraper")
    captured = capfd.readouterr()
    assert "::notice title=Scraper::Done. 3 new article(s) written." in captured.out


def test_report_notice_escapes_workflow_chars(
    capfd: pytest.CaptureFixture[str],
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """% and CR/LF must be escaped per GitHub Actions workflow command spec."""
    monkeypatch.setenv("GITHUB_ACTIONS", "true")
    report_notice("50% done\r\nnewline")
    report_notice("msg", title="T%\r\n")
    captured = capfd.readouterr()
    assert "50%25 done%0D%0Anewline" in captured.out
    assert "title=T%25%0D%0A::msg" in captured.out


def test_report_group_emits_group_commands(
    capfd: pytest.CaptureFixture[str],
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("GITHUB_ACTIONS", "true")
    with report_group("My Group"):
        print("inside")
    captured = capfd.readouterr()
    assert "::group::My Group" in captured.out
    assert "::endgroup::" in captured.out
    assert "inside" in captured.out


def test_write_step_summary_noop_without_env(tmp_path: Path) -> None:
    """When GITHUB_STEP_SUMMARY is unset, nothing is written and it returns False."""
    with pytest.MonkeyPatch().context() as mp:
        mp.delenv("GITHUB_STEP_SUMMARY", raising=False)
        written = write_step_summary("## Summary\n\nSome content.")
        assert written is False


def test_write_step_summary_appends_markdown(tmp_path: Path) -> None:
    """Content is appended (with a trailing newline) to the summary file."""
    summary_file = tmp_path / "summaries" / "step_summary.md"
    first_block = """\
### Scrape summary

| Site | New articles |
| --- | --- |
| Acme | 3 |
"""
    with pytest.MonkeyPatch().context() as mp:
        mp.setenv("GITHUB_STEP_SUMMARY", str(summary_file))
        ok = write_step_summary(first_block)
        assert ok is True
        # Second call should append, not overwrite
        ok2 = write_step_summary("- total: 3")
        assert ok2 is True

    assert summary_file.exists()
    content = summary_file.read_text(encoding="utf-8")
    assert "### Scrape summary" in content
    assert "- total: 3" in content
    # appended content keeps its own trailing newline
    assert content.endswith("\n")


def test_write_step_summary_adds_trailing_newline(tmp_path: Path) -> None:
    """A block without a trailing newline gets one added."""
    summary_file = tmp_path / "step_summary.md"
    with pytest.MonkeyPatch().context() as mp:
        mp.setenv("GITHUB_STEP_SUMMARY", str(summary_file))
        write_step_summary("no newline here")
    assert summary_file.read_text(encoding="utf-8") == "no newline here\n"


def test_write_step_summary_returns_false_on_oserror(tmp_path: Path) -> None:
    """A missing/unwritable target is handled gracefully (returns False)."""
    with pytest.MonkeyPatch().context() as mp:
        mp.setenv("GITHUB_STEP_SUMMARY", str(tmp_path / "nope" / "missing.md"))
        # Parent dir cannot be created (force a directory conflict)
        conflict = tmp_path / "nope"
        conflict.write_text("I am a file, not a directory")
        written = write_step_summary("content")
        assert written is False
