# testing/TestCreateLinearGuesses.py
import unittest
import itertools
import numpy as np
import os
import sys
import json

with open(os.path.join("..", "parameters.json"), "r") as parameters_file:
    parameters_data = json.load(parameters_file)

print(json.dumps(parameters_data))

repository_path = parameters_data["repository_path"]
print(repository_path)

sys.path.insert(0, repository_path)
import visualizer, util

test_figures_directory = os.path.join(repository_path, "testing", "test_figures", "create_linear_guesses")
os.makedirs(test_figures_directory, exist_ok=True)

class TestCreateLinearGuesses(unittest.TestCase):
    def plot_and_save(self, linear_definitions, test_name):
        x_values = np.linspace(0,10,100)
        figure_path = os.path.join(test_figures_directory, f"{test_name}.png")
        visualizer.plot_lines(x_values, linear_definitions, figure_path)

    def test_normal_range_as_tuples(self):
        # Test for normal range with return_dictionary=False
        result = util.create_linear_guesses(0, 10, 2, 0, 10, 2, return_dictionary=False)
        self.plot_and_save(result, 'result_normal_range_as_tuples')
        expected_combinations = list(itertools.product(range(0, 10, 2), range(0, 10, 2)))
        self.plot_and_save(expected_combinations, 'expected_normal_range_as_tuples')
        self.assertEqual(result, expected_combinations)

    def test_uneven_range_as_tuples(self):
        # Test for uneven range with return_dictionary=False
        result = util.create_linear_guesses(0, 5, 3, 0, 5, 3, return_dictionary=False)
        self.plot_and_save(result, 'result_uneven_range_as_tuples')
        expected_combinations = list(itertools.product(range(0, 5, 3), range(0, 5, 3)))
        self.plot_and_save(result, 'expected_uneven_range_as_tuples')
        self.assertEqual(result, expected_combinations)

    def test_normal_range_as_dicts(self):
        # Test for normal range with return_dictionary=True
        result = util.create_linear_guesses(0, 10, 2, 0, 10, 2, return_dictionary=True)
        expected_combinations = [{'slope': m, 'y_intercept': b} for m in range(0, 10, 2) for b in range(0, 10, 2)]
        self.assertEqual(result, expected_combinations)

    def test_uneven_range_as_dicts(self):
        # Test for uneven range with return_dictionary=True
        result = util.create_linear_guesses(0, 5, 3, 0, 5, 3, return_dictionary=True)
        expected_combinations = [{'slope': m, 'y_intercept': b} for m in range(0, 5, 3) for b in range(0, 5, 3)]
        self.assertEqual(result, expected_combinations)

if __name__ == '__main__':
    unittest.main()