import unittest

from or_aml_simulator import generate_transactions, project_info


class ProjectSmokeTest(unittest.TestCase):
    def test_project_metadata(self) -> None:
        self.assertEqual(project_info()["status"], "starter")

    def test_generation_is_reproducible_and_labelled(self) -> None:
        first = generate_transactions(seed=7, normal_count=2)
        second = generate_transactions(seed=7, normal_count=2)
        self.assertEqual(first, second)
        self.assertEqual(
            {row["scenario"] for row in first},
            {"normal", "cycle", "pass_through", "structuring"},
        )
        self.assertEqual(len({row["id"] for row in first}), len(first))



if __name__ == "__main__":
    unittest.main()

