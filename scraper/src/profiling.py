"""Lightweight call profiling utilities.

Provides :func:`profiled`, a decorator that records *how many times* a
function is invoked and the *cumulative wall-clock time* spent executing it.
On interpreter exit, a summary of every profiled function is printed to
stderr.

The decorator is thread-safe and works on plain functions, bound methods, and
coroutine functions (async/await). When decorating an ``async`` callable the
timer covers the full ``await`` rather than just the instant the coroutine is
created.
"""

from __future__ import annotations

import asyncio
import atexit
import sys
import threading
import time
from collections.abc import Callable
from dataclasses import dataclass, field
from functools import wraps
from typing import Any

# Collected statistics, in decoration order, guarded by ``_registry_lock``.
# Decorators are normally applied at import time (single-threaded), but the
# lock keeps things correct if a decorated callable happens to be created or
# destroyed while the process is shutting down.
_registry: list[_Stats] = []
_registry_lock = threading.Lock()


@dataclass
class _Stats:
    """Accumulated statistics for a single profiled callable."""

    name: str
    calls: int = 0
    total_time: float = 0.0
    # min_time starts at +inf (first call sets it); max_time starts at 0.
    min_time: float = float("inf")
    max_time: float = 0.0
    _lock: threading.Lock = field(default_factory=threading.Lock, repr=False)


def _record(stats: _Stats, start: float) -> None:
    """Record one completed call: count, elapsed time, and per-call min/max."""
    elapsed = time.perf_counter() - start
    with stats._lock:
        stats.calls += 1
        stats.total_time += elapsed
        if elapsed < stats.min_time:
            stats.min_time = elapsed
        if elapsed > stats.max_time:
            stats.max_time = elapsed


def profiled[T](func: Callable[..., T]) -> Callable[..., T]:
    """Decorate *func* so its call count and cumulative runtime are tracked.

    On interpreter exit, :func:`print_profile_stats` emits a summary to stderr
    for every function decorated with :func:`profiled`. The decorator handles
    both synchronous and asynchronous (``async def``) callables; for the latter
    the measured time spans the full ``await``.
    """
    stats = _Stats(name=f"{func.__module__}.{func.__qualname__}")
    with _registry_lock:
        _registry.append(stats)

    if asyncio.iscoroutinefunction(func):

        @wraps(func)
        async def async_wrapper(*args: Any, **kwargs: Any) -> T:
            start = time.perf_counter()
            try:
                return await func(*args, **kwargs)
            finally:
                # Count the call and accumulate time even if it raised, so we
                # capture failures in the statistics too.
                _record(stats, start)

        async_wrapper.__profile_stats__ = stats  # type: ignore[attr-defined]
        return async_wrapper

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> T:
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            _record(stats, start)

    # Expose the live stats object for programmatic introspection (e.g. tests).
    wrapper.__profile_stats__ = stats  # type: ignore[attr-defined]
    return wrapper


def print_profile_stats(stream: Any = sys.stderr) -> None:
    """Print accumulated profiling statistics to *stream*.

    Called automatically at interpreter exit; safe to invoke manually, e.g.
    from tests.
    """
    with _registry_lock:
        snapshot = list(_registry)

    if not snapshot:
        return

    name_w = max(len("Function"), max(len(s.name) for s in snapshot))
    header = (
        f"{'Calls':>7}  {'Total (s)':>11}  {'Avg (s)':>11}  "
        f"{'Min (s)':>11}  {'Max (s)':>11}  {'Function':<{name_w}}"
    )
    separator = "-" * len(header)

    lines = ["=== Profiling statistics ===", "", header, separator]
    for stats in snapshot:
        if stats.calls:
            avg = stats.total_time / stats.calls
            mn = stats.min_time
            mx = stats.max_time
        else:
            avg = 0.0
            mn = 0.0
            mx = 0.0
        lines.append(
            f"{stats.calls:>7}  {stats.total_time:>11.4f}  {avg:>11.4f}  "
            f"{mn:>11.4f}  {mx:>11.4f}  {stats.name:<{name_w}}"
        )
    lines.append("")
    print("\n".join(lines), file=stream)


# Emit the summary automatically when the interpreter exits normally. An
# ``atexit`` handler fires on regular shutdown (including ``asyncio.run``),
# so the scraper's end-of-process summary is covered.
atexit.register(print_profile_stats)
