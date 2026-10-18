"""Public API for OR AML Simulator."""

from .generator import generate_dataset, generate_transactions

__version__ = "0.2.0"


def project_info() -> dict[str, str]:
    return {
        "name": "OR AML Simulator",
        "focus": "Reproducible synthetic AML scenarios",
        "status": "reference-prototype",
    }


__all__ = ["generate_dataset", "generate_transactions", "project_info"]

