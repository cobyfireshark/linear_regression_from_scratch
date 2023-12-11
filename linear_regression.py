# linear_regression.py
import os
import util
import logging

def predict(row, coefficients):
    y_hat = coefficients[0]
    for i in range(len(row)-1):
        y_hat += coefficients[i+1] * row[i]
        
    return y_hat

def coefficients_sgd(train, l_rate, n_epoch):
    coefficient = [0.0 for i in range(len(train[0]))]
    for epoch in range(n_epoch):
        sum_error = 0
        

def main():
    # Initialize logging
    log_path = os.path.join("var", "log", "decision_tree", "decision_tree.log")
    util.initialize_logging(False, log_path)
    logging.info(f"Logging initialized, output file: {log_path}")

    dataset = [
        [1,1],
        [2,3],
        [4,3],
        [3,2],
        [5,5]
    ]

    coefficients = [0.4,0.8]

    for row in dataset:
        y_hat = predict(row, coefficients)
        print("Expected=%.3f, Predicted=%.3f" % (row[-1], y_hat))

if __name__ == "__main__":
    main()
