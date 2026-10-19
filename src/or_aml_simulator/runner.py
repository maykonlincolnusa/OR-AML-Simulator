"""Validated boundary used by the CLI and HTTP adapter."""
from .generator import generate_benchmark, generate_dataset


def run(payload):
    if not isinstance(payload, dict) or set(payload) - set(["seed","normal_count","currency","action","test_percent"]):
        raise ValueError("request must be an object containing only documented fields")
    payload = dict(payload)
    action = payload.pop("action", "dataset")
    if action == "benchmark":
        return generate_benchmark(**payload)
    if action != "dataset" or "test_percent" in payload:
        raise ValueError("unknown action or unexpected benchmark option")
    return generate_dataset(**payload)
