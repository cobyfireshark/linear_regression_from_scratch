import argparse
import os
import util
import logging
import pandas as pd
import visualizer
import cost_function
import json

linear_regression_log_path = os.path.join("/var", "log", "regression", "linear_regression_gd.log")
util.initialize_logging(linear_regression_log_path)

def take_gradient_descent_step(data, w, b, learning_rate):
    dw = 0  # Gradient with respect to w
    db = 0  # Gradient with respect to b
    m = len(data)  # Number of data points

    logging.info(f"data: {data}")

    for i in range(len(data)):
        x, y = data.iloc[i]['x'], data.iloc[i]['y']
        fw_b_x = w * x + b  # Prediction
        error = fw_b_x - y  # Error term
        dw += error * x  # Partial derivative with respect to w
        db += error  # Partial derivative with respect to b

    # Average out the gradients
    dw /= m
    db /= m
    logging.info(f"dw:\n{dw}\ndb:\n{db}")

    # Update the parameters
    w = w - learning_rate * dw
    b = b - learning_rate * db

    return w, b

def gradient_descent_to_convergence(data, w_initial, b_initial, learning_rate, convergence):
    linear_guess_initial = [{'slope': w_initial, 'y_intercept': b_initial}]
    logging.info(f"initial linear guess:\n{json.dumps(linear_guess_initial, indent=4)}")
    predictions_initial = cost_function.make_linear_predictions(data, linear_guess_initial)
    cost = cost_function.solve_cost_function(data, predictions_initial)
    i=0
    costs_series = {}
    cost_key = f"({w_initial}, {b_initial})"
    costs_series[i] = cost[cost_key]
    epsilon = 100
    w = w_initial
    b = b_initial
    while epsilon>=convergence:
        i+=1
        if i >= 200:
            logging.info("failed to converge after 100 iteration steps")
            break
        w, b = take_gradient_descent_step(data, w, b, learning_rate)
        linear_guess = [{'slope': w, 'y_intercept': b}]
        predictions = cost_function.make_linear_predictions(data, linear_guess)
        cost = cost_function.solve_cost_function(data, predictions)
        cost_key = f"({w}, {b})"
        costs_series[i] = cost[cost_key]
        epsilon = abs(costs_series[i] - costs_series[i-1])
        logging.info(f"epsilon={epsilon}")
    logging.info(f"i: {i}")
    return w,b

def main(training_set_path):
    logging.info(f"main(training_set_path={training_set_path})")
    input_data = pd.read_csv(training_set_path, header=0)
    logging.info(f"input_data:\n{input_data}")
    input_data_figure_path = os.path.join("figures", "input_data.png")
    visualizer.plot_xy_data(input_data, input_data_figure_path)
    logging.info(f"figure created of input data at {input_data_figure_path}")
    learning_rate = 0.01
    w = -2
    b = 9
    convergence = 0.01
    w, b = gradient_descent_to_convergence(input_data, w, b, learning_rate, convergence)
    logging.info(f"(w,b) = ({w},{b})")
    prediction_line_figure_path = os.path.join("figures", "prediction_line.png")
    visualizer.plot_lines(input_data.iloc[:,0], [(w,b)], prediction_line_figure_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()    
    parser.add_argument("--training-set-path", required=True, help="Your training sets full path")
    args = parser.parse_args()

    main(args.training_set_path)