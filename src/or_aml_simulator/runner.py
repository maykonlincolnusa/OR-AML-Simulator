"""Validated boundary used by the CLI and HTTP adapter."""
from .generator import generate_dataset


def run(payload):
    if not isinstance(payload, dict) or set(payload) - set(["seed","normal_count","currency"]):
        raise ValueError("request must be an object containing only documented fields")
    return generate_dataset(**payload)
