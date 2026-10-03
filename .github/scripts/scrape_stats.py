#!/usr/bin/env -s uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "httpx",
#   "matplotlib",
# ]
# ///

"""Build the run‑duration + frequency + per‑job breakdown chart for a workflow.

Output (PNG) is committed to ``docs/scrape_stats.png`` by ``stats.yml``.

Panel 1: per‑run duration (scatter, coloured by conclusion) + a 10‑run rolling
         average.
Panel 2: runs per week (frequency).
Panel 3: stacked per‑job time breakdown for the most recent runs, so you can
         see how long each job (e.g. ``scrape`` vs ``build-and-deploy``) took.
"""

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

# How far back to pull run metadata. GitHub returns newest-first; we page
# until either we run out of runs or hit this cap, whichever comes first.
MAX_RUNS = 800

# How many recent runs to enrich with per‑job timing. Fetched from the jobs
# endpoint (one extra request per run), so keep this modest to stay well
# within the GITHUB_TOKEN rate budget.
JOB_BREAKDOWN_WINDOW = 60

CONCLUSION_COLORS = {
    "success": "#2ea44f",
    "failure": "#d73a49",
    "cancelled": "#8b949e",
    "timed_out": "#e36209",
}
DEFAULT_COLOR = "#8b949e"

# Preferred colors for the two scrape.yml jobs. The articles-scrape job
# ("Scrape articles") is orange; the deploy job ("Build site and deploy")
# is purple. The GitHub jobs API returns the workflow `name:` fields, so we
# match by exact name and by keyword (robust to display-name tweaks);
# anything else falls back to the cycle below.
JOB_COLORS_BY_NAME = {
    "Scrape articles": "#d29922",  # orange — the articles-scrape job
    "Build site and deploy": "#8250df",  # purple
}
JOB_COLOR_KEYWORDS: dict[str, str] = {
    "article": "#d29922",
    "scrape": "#d29922",
    "build": "#8250df",
    "deploy": "#8250df",
}
# Fallback palette for any other job names, chosen for mutual contrast.
JOB_COLOR_CYCLE = ["#0969da", "#8250df", "#d29922", "#1f734c", "#cb2439", "#54aeff"]


def job_color(name: str, index: int) -> str:
    """Bar color for a job display name: exact name, then keyword, then cycle."""
    if name in JOB_COLORS_BY_NAME:
        return JOB_COLORS_BY_NAME[name]
    low = name.lower()
    for kw, color in JOB_COLOR_KEYWORDS.items():
        if kw in low:
            return color
    return JOB_COLOR_CYCLE[index % len(JOB_COLOR_CYCLE)]


def gha(level: str, msg: str) -> None:
    if os.environ.get("GITHUB_ACTIONS"):
        print(f"::{level}::{msg}")
    else:
        print(msg)


def _headers() -> dict[str, str]:
    headers = {"Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def fetch_runs(
    repo: str, workflow_id: str, max_runs: int, client: httpx.Client
) -> list[dict]:
    runs: list[dict] = []
    page = 1
    while len(runs) < max_runs:
        r = client.get(
            f"https://api.github.com/repos/{repo}/actions/workflows/{workflow_id}/runs",
            params={
                "per_page": 100,
                "page": page,
                "status": "completed",
            },
            headers=_headers(),
            timeout=30,
        )
        r.raise_for_status()
        data = r.json().get("workflow_runs", [])
        if not data:
            break
        runs.extend(data)
        page += 1
    return runs[:max_runs]


def fetch_jobs(client: httpx.Client, repo: str, run_id: int) -> list[dict]:
    """All jobs for a run, paginated (capped at 5 pages -> 500 jobs)."""
    jobs: list[dict] = []
    page = 1
    while page <= 5:
        r = client.get(
            f"https://api.github.com/repos/{repo}/actions/runs/{run_id}/jobs",
            params={"per_page": 100, "page": page},
            headers=_headers(),
            timeout=30,
        )
        r.raise_for_status()
        page_jobs = r.json().get("jobs", [])
        if not page_jobs:
            break
        jobs.extend(page_jobs)
        if len(page_jobs) < 100:
            break
        page += 1
    return jobs


def parse_dt(s: str) -> datetime:
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def _job_minutes(job: dict) -> float | None:
    """Wall-clock duration of a job in minutes, or ``None`` if untimed/skipped."""
    conclusion = job.get("conclusion") or ""
    if conclusion == "skipped":
        return None
    start = job.get("run_started_at") or job.get("started_at")
    end = job.get("completed_at")
    if not start or not end:
        return None
    try:
        return max((parse_dt(end) - parse_dt(start)).total_seconds() / 60.0, 0.0)
    except (ValueError, TypeError):
        return None


def main() -> None:
    repo = sys.argv[1] if len(sys.argv) > 1 else REPO
    workflow_id = sys.argv[2] if len(sys.argv) > 2 else WORKFLOW_ID
    gha("notice", f"Fetching runs for {repo} / {workflow_id}...")

    with httpx.Client() as client:
        runs = fetch_runs(repo, workflow_id, MAX_RUNS, client)
    gha("notice", f"  Fetched {len(runs)} completed runs")

    if not runs:
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.text(
            0.5,
            0.5,
            "No workflow run data yet",
            ha="center",
            va="center",
            transform=ax.transAxes,
            fontsize=13,
            color="#888",
        )
        ax.set_title(f"{workflow_id} — {repo}", fontsize=13, pad=12)
        ax.spines[["top", "right", "left", "bottom"]].set_visible(False)
        ax.set_xticks([])
        ax.set_yticks([])
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(OUTPUT, dpi=150, bbox_inches="tight")
        gha("warning", f"  No runs yet, saved placeholder to {OUTPUT}")
        return

    # (start, duration_minutes, conclusion, run_id)
    records: list[tuple[datetime, float, str, int]] = []
    for run in runs:
        start_raw = run.get("run_started_at") or run["created_at"]
        end_raw = run["updated_at"]
        start = parse_dt(start_raw)
        end = parse_dt(end_raw)
        duration_min = max((end - start).total_seconds() / 60.0, 0.0)
        records.append(
            (start, duration_min, run.get("conclusion") or "unknown", int(run["id"]))
        )

    records.sort(key=lambda r: r[0])
    durations = [r[1] for r in records]
    total = len(records)
    avg = sum(durations) / total
    longest = max(records, key=lambda r: r[1])

    gha("notice", f"  Total runs plotted: {total}")
    gha("notice", f"  Average duration:   {avg:.1f} min")
    gha("notice", f"  Longest run:        {longest[1]:.1f} min on {longest[0].date()}")

    # Weekly run counts, for the frequency panel
    weekly_counts: dict[datetime, int] = defaultdict(int)
    for start, _, _, _ in records:
        week_start = start - timedelta(days=start.weekday())
        week_start = datetime(
            week_start.year, week_start.month, week_start.day, tzinfo=timezone.utc
        )
        weekly_counts[week_start] += 1
    weeks = sorted(weekly_counts)
    week_totals = [weekly_counts[w] for w in weeks]

    # Per-job breakdown for the most recent window. One jobs-endpoint call per
    # run, so we cap the window; degrade gracefully if any call fails.
    recent = records[-JOB_BREAKDOWN_WINDOW:]
    job_breakdown: list[dict[str, float]] = []  # per recent run, {job_name: min}
    job_names: list[str] = []
    seen: set[str] = set()
    with httpx.Client() as client:
        for start, _, _, run_id in recent:
            job_map: dict[str, float] = {}
            try:
                for job in fetch_jobs(client, repo, run_id):
                    name = job.get("name", "unknown")
                    mins = _job_minutes(job)
                    if mins is None:
                        continue
                    if name not in seen:
                        seen.add(name)
                        job_names.append(name)
                    job_map[name] = mins
            except (httpx.HTTPStatusError, httpx.RequestError) as exc:
                gha("warning", f"  Could not fetch jobs for run {run_id}: {exc}")
            job_breakdown.append(job_map)

    fig, (ax_dur, ax_freq, ax_jobs) = plt.subplots(
        3,
        1,
        figsize=(12, 10),
        gridspec_kw={"height_ratios": [2, 1, 1]},
    )
    ax_freq.sharex(ax_dur)

    # --- Panel 1: duration per run over time ---
    for conclusion in {r[2] for r in records}:
        xs = [r[0] for r in records if r[2] == conclusion]
        ys = [r[1] for r in records if r[2] == conclusion]
        ax_dur.scatter(
            xs,
            ys,
            s=14,
            color=CONCLUSION_COLORS.get(conclusion, DEFAULT_COLOR),
            label=conclusion,
            alpha=0.8,
            edgecolors="none",
        )

    # Rolling average line (window of 10 runs) to show the trend
    window = 10
    if total >= window:
        roll_x = [records[i][0] for i in range(window - 1, total)]
        roll_y = [
            sum(durations[i - window + 1 : i + 1]) / window
            for i in range(window - 1, total)
        ]
        ax_dur.plot(
            roll_x,
            roll_y,
            color="#0969da",
            linewidth=1.5,
            label=f"{window}-run avg",
        )

    ax_dur.set_title(
        f"{workflow_id} — duration & frequency — {repo}", fontsize=13, pad=12
    )
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
    ax_freq.xaxis.set_major_locator(mdates.AutoDateLocator(minticks=20, maxticks=27))
    ax_freq.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
    # Show the shared date axis' labels only on the runs/week panel (the bottom
    # of the duration/runs-week pair). fig.autofmt_xdate is avoided on purpose:
    # with the index-based jobs panel anchored below, it blanks the shared date
    # labels entirely (including the runs/week panel).
    ax_dur.tick_params(axis="x", labelbottom=False)

    # --- Panel 3: per-job time breakdown (most recent runs) ---
    if job_breakdown and job_names:
        color_for: dict[str, str] = {}
        for i, name in enumerate(job_names):
            color_for[name] = job_color(name, i)
        xs = list(range(len(job_breakdown)))
        bottoms = [0.0] * len(job_breakdown)
        for name in job_names:
            heights = [jb.get(name, 0.0) for jb in job_breakdown]
            ax_jobs.bar(
                xs,
                heights,
                bottom=bottoms,
                color=color_for[name],
                width=0.8,
                label=name,
            )
            bottoms = [b + h for b, h in zip(bottoms, heights)]
        # Label roughly every k-th bar so the full 60-run window doesn't
        # crowd the x-axis; always include the most recent run.
        n = len(job_breakdown)
        step = max(1, n // 12)
        tick_idx = list(range(0, n, step))
        if (n - 1) not in tick_idx:
            tick_idx.append(n - 1)
        ax_jobs.set_xticks([xs[i] for i in tick_idx])
        ax_jobs.set_xticklabels(
            [recent[i][0].strftime("%m-%d") for i in tick_idx],
            rotation=45,
            ha="right",
            fontsize=8,
        )
        ax_jobs.set_ylabel("Minutes", fontsize=10)
        ax_jobs.set_title(
            f"Job-level time breakdown — last {len(job_breakdown)} runs",
            fontsize=11,
            pad=10,
        )
        ax_jobs.spines[["top", "right"]].set_visible(False)
        ax_jobs.grid(axis="y", color="#e0e0e0", linewidth=0.5)
        ax_jobs.set_axisbelow(True)
        ax_jobs.legend(fontsize=8, frameon=False, loc="upper left")
    else:
        ax_jobs.text(
            0.5,
            0.5,
            "No per-job run data available",
            ha="center",
            va="center",
            transform=ax_jobs.transAxes,
            fontsize=11,
            color="#888",
        )
        ax_jobs.set_xticks([])
        ax_jobs.set_yticks([])
        ax_jobs.spines[["top", "right", "left", "bottom"]].set_visible(False)

    # Materialise tick labels (incl. shared date ticks) so we can rotate them
    # deterministically — fig.autofmt_xdate cannot be used alongside the extra
    # index-based jobs panel without blanking the shared date labels.
    fig.canvas.draw()
    plt.setp(ax_freq.get_xticklabels(), rotation=45, ha="right")
    plt.setp(ax_jobs.get_xticklabels(), rotation=45, ha="right")
    # Give the (now-visible) date labels on the middle panel room above the
    # jobs panel — without enough hspace they bleed into panel 3. The old
    # bottom=0.14/hspace=0.2 layout let them protrude ~34px into the jobs
    # axes box; 0.2/0.6 leaves ~20px of clearance for the denser real run set.
    fig.subplots_adjust(bottom=0.2, hspace=0.6)
    fig.savefig(OUTPUT, dpi=150, bbox_inches="tight")
    gha("notice", f"  Saved to {OUTPUT}")


if __name__ == "__main__":
    main()
