from or_aml_simulator import generate_benchmark


def test_benchmark_is_reproducible_and_entity_disjoint():
    first = generate_benchmark(seed=17, normal_count=50, test_percent=40)
    second = generate_benchmark(seed=17, normal_count=50, test_percent=40)
    assert first["manifest_sha256"] == second["manifest_sha256"]
    train_ids, test_ids = set(first["train_transaction_ids"]), set(first["test_transaction_ids"])
    assert not train_ids & test_ids
    transactions = {row["id"]: row for row in first["transactions"]}
    train_accounts = {transactions[key][field] for key in train_ids
                      for field in ("source_account_id", "destination_account_id")}
    test_accounts = {transactions[key][field] for key in test_ids
                     for field in ("source_account_id", "destination_account_id")}
    assert not train_accounts & test_accounts
