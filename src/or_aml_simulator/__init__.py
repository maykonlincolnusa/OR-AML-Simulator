"""Public API for OR AML Simulator."""

from .generator import generate_benchmark, generate_dataset, generate_transactions

__version__ = "0.3.0"


def project_info() -> dict[str, str]:
    return {
        "name": "OR AML Simulator",
        "focus": "Reproducible synthetic AML scenarios",
        "status": "reference-prototype",
    }


__all__ = ["generate_benchmark", "generate_dataset", "generate_transactions", "project_info"]

