# OR AML Simulator

Deterministic synthetic data generation for AML engineering, demonstrations, and regression tests without using real customer data.

## Why it matters

Financial-crime teams need reproducible datasets to test rules, explain behavior, and compare system changes. This project injects known scenarios while keeping labels separate from transaction features to reduce accidental label leakage.

## Current capabilities

- Seeded generation using integer cents for reproducible money values.
- Normal activity plus cycle, pass-through, structuring, fan-in, and fan-out scenarios.
- Separate entities, accounts, transactions, and ground-truth labels.
- Stable identifiers, UTC timestamps, configurable currency, JSON or CSV output.
- Connected-component train/test manifests that prevent the same network leaking across splits.
- Strict validation, deterministic CLI, optional authenticated API, Docker image, and CI.

## Run

```sh
python -m pip install -e '.[dev,api]'
python -m or_aml_simulator --demo
python -m or_aml_simulator --demo --format csv
pytest -q && ruff check src tests
```

API: set `OR_API_KEY` to at least 16 characters, run `uvicorn or_aml_simulator.api:create_app --factory`, then POST the JSON in `examples/request.json` to `/v1/analyze` with `X-API-Key`.

## Limitations and roadmap

Set `action` to `benchmark` to create a reproducible split and manifest fingerprint. Generated labels describe injected patterns, not crime. The dataset is not statistically representative of any institution and must not be used to claim model accuracy. Next steps include configurable populations and channels, data-quality defects, temporal drift, and validation against privacy and fairness requirements.
