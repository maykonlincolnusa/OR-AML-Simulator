"""Starter package for OR AML Simulator."""

from .generator import generate_transactions

__version__ = "0.1.0"


def project_info() -> dict[str, str]:
    return {
        "name": "OR AML Simulator",
        "focus": "Reproducible synthetic AML scenarios",
        "status": "starter",
    }


__all__ = ["generate_transactions", "project_info"]

