"""Seeded synthetic fixtures; labels describe injected scenarios, not real crime."""
from __future__ import annotations

import random
from datetime import datetime, timedelta, timezone
from decimal import Decimal

from .validation import currency as validate_currency
from .validation import integer


def generate_transactions(seed=42, normal_count=10, currency="BRL"):
    integer(seed, "seed", 0, 2147483647)
    integer(normal_count, "normal_count", 0, 9985)
    validate_currency(currency)
    rng = random.Random(seed)
    start = datetime(2026, 1, 1, 12, tzinfo=timezone.utc)
    rows = []

    def add(source, destination, cents, minute, label):
        txid = f"tx-{len(rows) + 1:06d}"
        rows.append({
            "id": txid, "source_account_id": source, "destination_account_id": destination,
            "amount": format(Decimal(cents) / Decimal("100"), ".2f"), "currency": currency,
            "occurred_at": (start + timedelta(minutes=minute)).isoformat(),
            "scenario": label, "source_system": "synthetic", "external_id": txid,
        })

    for index in range(normal_count):
        add(f"normal-{rng.randint(1, 8)}", f"normal-{rng.randint(9, 16)}",
            rng.randint(2500, 180000), index * 20, "normal")
    for source, target, cents, minute in [
        ("cycle-a", "cycle-b", 500000, 300), ("cycle-b", "cycle-c", 480000, 305),
        ("cycle-c", "cycle-a", 460000, 310),
    ]:
        add(source, target, cents, minute, "cycle")
    add("pass-in", "pass-hub", 800000, 400, "pass_through")
    add("pass-hub", "pass-out", 780000, 405, "pass_through")
    for index, cents in enumerate((320000, 310000, 300000, 290000)):
        add("split-origin", f"split-{index + 1}", cents, 500 + index * 5, "structuring")
    for index in range(3):
        add(f"fan-sender-{index}", "fan-hub", 100000, 600 + index, "fan_in")
        add("fan-out-hub", f"fan-recipient-{index}", 100000, 700 + index, "fan_out")
    return sorted(rows, key=lambda r: (r["occurred_at"], r["id"]))


def generate_dataset(seed=42, normal_count=10, currency="BRL"):
    rows = generate_transactions(seed, normal_count, currency)
    accounts = sorted({r[key] for r in rows for key in ("source_account_id", "destination_account_id")})
    return {
        "schema_version": "2.0", "seed": seed, "synthetic": True,
        "entities": [{"id": "entity-" + a, "kind": "organization", "display_name": "Synthetic " + a} for a in accounts],
        "accounts": [{"id": a, "entity_id": "entity-" + a, "institution": "SYNTHETIC_BANK"} for a in accounts],
        # Keep labels outside the transaction features to avoid label leakage.
        "transactions": [{k: v for k, v in r.items() if k != "scenario"} for r in rows],
        "labels": [{"transaction_id": r["id"], "scenario": r["scenario"]} for r in rows],
    }

