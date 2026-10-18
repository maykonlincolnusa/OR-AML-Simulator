"""Deterministic synthetic transactions for local AML experiments."""

from __future__ import annotations

import random
from datetime import datetime, timedelta, timezone


def generate_transactions(seed: int = 42, normal_count: int = 10) -> list[dict[str, object]]:
    if normal_count < 0:
        raise ValueError("normal_count must be non-negative")

    rng = random.Random(seed)
    start = datetime(2026, 1, 1, 12, tzinfo=timezone.utc)
    rows: list[dict[str, object]] = []

    def add(source: str, destination: str, amount: float, minute: int, label: str) -> None:
        rows.append(
            {
                "id": f"tx-{len(rows) + 1:04d}",
                "source_account_id": source,
                "destination_account_id": destination,
                "amount": f"{amount:.2f}",
                "currency": "BRL",
                "occurred_at": (start + timedelta(minutes=minute)).isoformat(),
                "scenario": label,
            }
        )

    for index in range(normal_count):
        source = f"normal-{rng.randint(1, 8)}"
        destination = f"normal-{rng.randint(9, 16)}"
        add(source, destination, rng.uniform(25, 1800), index * 20, "normal")

    add("cycle-a", "cycle-b", 5000, 300, "cycle")
    add("cycle-b", "cycle-c", 4800, 305, "cycle")
    add("cycle-c", "cycle-a", 4600, 310, "cycle")
    add("pass-in", "pass-hub", 8000, 400, "pass_through")
    add("pass-hub", "pass-out", 7800, 405, "pass_through")
    for index, amount in enumerate((3200, 3100, 3000, 2900)):
        add("split-origin", f"split-{index + 1}", amount, 500 + index * 5, "structuring")
    return rows

