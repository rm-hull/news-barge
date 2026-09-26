#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "httpx",
#   "matplotlib",
# ]
# ///

import os
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

import httpx
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

REPO = "rm-hull/news-barge"
WORKFLOW_ID = "scrape.yml"
OUTPUT = Path(__file__).parents[2] / "docs" / "scrape_stats.png"

# How far back to pull. GitHub returns newest-first; we page until either
# we run out of runs or hit this cap, whichever comes first.
MAX_RUNS = 500

CONCLUSION_COLORS = {
    "success": "#2ea44f",
    "failure": "#d73a49",
    "cancelled": "#8b949e",
    "timed_out": "#e36209",
}
DEFAULT_COLOR = "#8b949e"


def gha(level: str, msg: str) -> None:
    if os.environ.get("GITHUB_ACTIONS"):
        print(f"::{level}::{msg}")
    else:
        print(msg)


def fetch_runs(repo: str, workflow_id: str, max_runs: int) -> list[dict]:
    runs = []
    page = 1
    token = os.environ.get("GITHUB_TOKEN")
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    with httpx.Client() as client:
        while len(runs) < max_runs:
            r = client.get(
                f"https://api.github.com/repos/{repo}/actions/workflows/{workflow_id}/runs",
                params={
                    "per_page": 100,
                    "page": page,
                    "status": "completed",
                },
                headers=headers,
                timeout=30,
            )
            r.raise_for_status()
            data = r.json().get("workflow_runs", [])
            if not data:
                break
            runs.extend(data)
            if len(data) < 100:
                break
            page += 1
    return runs[:max_runs]


def parse_dt(s: str) -> datetime:
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def main():
    repo = sys.argv[1] if len(sys.argv) > 1 else REPO
    workflow_id = sys.argv[2] if len(sys.argv) > 2 else WORKFLOW_ID
    gha("notice", f"Fetching runs for {repo} / {workflow_id}...")

    runs = fetch_runs(repo, workflow_id, MAX_RUNS)
    gha("notice", f"  Fetched {len(runs)} completed runs")

    if not runs:
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.text(
            0.5, 0.5, "No workflow run data yet",
            ha="center", va="center", transform=ax.transAxes,
            fontsize=13, color="#888",
        )
        ax.set_title(f"{workflow_id} — {repo}", fontsize=13, pad=12)
        ax.spines[["top", "right", "left", "bottom"]].set_visible(False)
        ax.set_xticks([])
        ax.set_yticks([])
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(OUTPUT, dpi=150, bbox_inches="tight")
        gha("warning", f"  No runs yet, saved placeholder to {OUTPUT}")
        return

    points = []  # (start_dt, duration_minutes, conclusion)
    for run in runs:
        start_raw = run.get("run_started_at") or run["created_at"]
        end_raw = run["updated_at"]
        start = parse_dt(start_raw)
        end = parse_dt(end_raw)
        duration_min = max((end - start).total_seconds() / 60.0, 0)
        points.append((start, duration_min, run.get("conclusion") or "unknown"))

    points.sort(key=lambda p: p[0])
    durations = [p[1] for p in points]
    total = len(points)
    avg = sum(durations) / total
    longest = max(points, key=lambda p: p[1])

    gha("notice", f"  Total runs plotted: {total}")
    gha("notice", f"  Average duration:   {avg:.1f} min")
    gha("notice", f"  Longest run:        {longest[1]:.1f} min on {longest[0].date()}")

    # Weekly run counts, for the frequency panel
    weekly_counts: dict[datetime, int] = defaultdict(int)
    for start, _, _ in points:
        week_start = start - timedelta(days=start.weekday())
        week_start = datetime(week_start.year, week_start.month, week_start.day, tzinfo=timezone.utc)
        weekly_counts[week_start] += 1
    weeks = sorted(weekly_counts)
    week_totals = [weekly_counts[w] for w in weeks]

    fig, (ax_dur, ax_freq) = plt.subplots(
        2, 1, figsize=(12, 8), sharex=True,
        gridspec_kw={"height_ratios": [2, 1]},
    )

    # --- Panel 1: duration per run over time ---
    for conclusion in {p[2] for p in points}:
        xs = [p[0] for p in points if p[2] == conclusion]
        ys = [p[1] for p in points if p[2] == conclusion]
        ax_dur.scatter(
            xs, ys, s=14,
            color=CONCLUSION_COLORS.get(conclusion, DEFAULT_COLOR),
            label=conclusion, alpha=0.8, edgecolors="none",
        )

    # Rolling average line (window of 10 runs) to show the trend
    window = 10
    if total >= window:
        roll_x = [points[i][0] for i in range(window - 1, total)]
        roll_y = [
            sum(durations[i - window + 1: i + 1]) / window
            for i in range(window - 1, total)
        ]
        ax_dur.plot(roll_x, roll_y, color="#0969da", linewidth=1.5, label=f"{window}-run avg")

    ax_dur.set_title(f"{workflow_id} — duration & frequency — {repo}", fontsize=13, pad=12)
    ax_dur.set_ylabel("Duration (minutes, log scale)", fontsize=10)
    ax_dur.set_yscale("log")
    ax_dur.yaxis.set_major_formatter(mticker.ScalarFormatter())
    ax_dur.yaxis.set_minor_formatter(mticker.NullFormatter())
    ax_dur.spines[["top", "right"]].set_visible(False)
    ax_dur.grid(axis="y", which="major", color="#e0e0e0", linewidth=0.5)
    ax_dur.set_axisbelow(True)
    ax_dur.legend(fontsize=8, frameon=False, loc="upper left")

    # --- Panel 2: runs per week (frequency) ---
    if weeks:
        width = 5.5  # days, slightly less than 7 so bars don't touch
        ax_freq.bar(weeks, week_totals, width=width, color="#54aeff", align="edge")
    ax_freq.set_ylabel("Runs / week", fontsize=10)
    ax_freq.set_xlabel("Date", fontsize=10)
    ax_freq.spines[["top", "right"]].set_visible(False)
    ax_freq.grid(axis="y", color="#e0e0e0", linewidth=0.5)
    ax_freq.set_axisbelow(True)
    ax_freq.xaxis.set_major_locator(mdates.AutoDateLocator())
    ax_freq.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
    fig.autofmt_xdate()

    fig.tight_layout()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT, dpi=150, bbox_inches="tight")
    gha("notice", f"  Saved to {OUTPUT}")


if __name__ == "__main__":
    main()