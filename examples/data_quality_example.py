"""Sanitized example of explicit data-quality flags."""

from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass(frozen=True)
class Observation:
    observed_at: datetime
    value: float | None


def quality_flags(obs: Observation, *, now: datetime, max_age: timedelta) -> set[str]:
    flags: set[str] = set()
    if obs.value is None:
        flags.add("MISSING")
    if now - obs.observed_at > max_age:
        flags.add("STALE")
    return flags or {"OK"}
