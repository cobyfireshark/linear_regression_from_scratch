# [repository_directory]/cost_function_vectorize.py
import util
import logging
import os
import json
import argparse
import pandas as pd
import visualizer
import util

cost_function_log_path = os.path.join("/var", "log", "regression", "cost_function.log")
util.initialize_logging(cost_function_log_path)

def solve_cost_function(data, predictions):
    # Using squared error cost function
    # J = 1/2m sum i=1 to m (error)^2
    logging.info("solve_cost_function()")
    m = len(data) # Number of data points
    actual_y = data.iloc[:, 1]

    costs = {}
    for key, predicted_y in predictions.items():
        error = predicted_y - actual_y
        squared_error = error ** 2
        cost = squared_error.sum() / (2*m)
        costs[key] = cost
    logging.info(f"costs:\n{json.dumps(costs, indent=4)}")
    return costs

def make_linear_predictions(data, linear_guesses):
    predictions = {}
    x = data.iloc[:,0]
    logging.info(f"x:\n{x}")
    for guess in linear_guesses:
        # logging.info(f"guess: {guess}")
        prediction = guess["slope"]*x+guess["y_intercept"]
        key = f"{guess['slope'],guess['y_intercept']}"
        predictions[key] = prediction
    # logging.info(f"predictions:\n{predictions}")
    return predictions

def main(training_set_path, dictionary_mode):
    logging.info(f"main(training_set_path={training_set_path})")
    input_data = pd.read_csv(training_set_path)
    input_data_figure_path = os.path.join("figures", "input_data.png")
    visualizer.plot_xy_data(input_data, input_data_figure_path)
    linear_guesses = util.create_linear_guesses()
    linear_guesses_tuples = [(entry["slope"], entry["y_intercept"]) for entry in linear_guesses]
    linear_guesses_figure_path = os.path.join("figures", "linear_guesses.png")
    visualizer.plot_lines(input_data.iloc[:,0], linear_guesses_tuples, linear_guesses_figure_path)
    linear_predictions = make_linear_predictions(input_data, linear_guesses)
    costs = solve_cost_function(input_data, linear_predictions)
    
    # Extract slope and y-intercept values and corresponding cost values
    slopes, y_intercepts = zip(*(eval(key) for key in costs.keys()))
    cost_values = list(costs.values())

    # Create a DataFrame for the cost values
    df = pd.DataFrame({'Slope': slopes, 'Y-intercept': y_intercepts, 'Cost': cost_values})
    cost_contour_map_figure_path = os.path.join("figures", "contour_map.png")
    visualizer.contour_map(df, cost_contour_map_figure_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()    
    parser.add_argument("--training-set-path", required=True, help="Your training sets full path")
    parser.add_argument("--dictionary-mode", action="store_true")
    args = parser.parse_args()

    main(args.training_set_path, args.dictionary_mode)