import unittest

from or_aml_simulator import generate_dataset, generate_transactions, project_info


class ProjectTest(unittest.TestCase):
    def test_generation_is_reproducible_and_labelled(self):
        first = generate_transactions(seed=7, normal_count=2)
        self.assertEqual(first, generate_transactions(seed=7, normal_count=2))
        self.assertEqual({row["scenario"] for row in first},
                         {"normal", "cycle", "pass_through", "structuring", "fan_in", "fan_out"})
        self.assertEqual(project_info()["status"], "reference-prototype")

    def test_dataset_separates_labels_from_features(self):
        dataset = generate_dataset(seed=7, normal_count=1, currency="USD")
        self.assertTrue(dataset["synthetic"])
        self.assertTrue(all("scenario" not in row for row in dataset["transactions"]))
        self.assertTrue(all(row["currency"] == "USD" for row in dataset["transactions"]))

    def test_rejects_invalid_currency(self):
        with self.assertRaises(ValueError):
            generate_dataset(currency="usd")


if __name__ == "__main__":
    unittest.main()
