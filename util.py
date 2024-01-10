# regression/util.py
import os
import logging
import itertools
import json
from csv import reader
import pandas as pd

# Set up basic logging configuration if no logging configuration is present
if not logging.getLogger().hasHandlers():
    logging.basicConfig(level=logging.INFO)

def create_linear_guesses(
    m_start=0,
    m_end=10,
    m_step=2,
    b_start=0,
    b_end=10,
    b_step=2,
    return_dictionary=False
):
    logging.info("util.create_linear_guesses()")

    if (m_end - m_start) % m_step != 0:
        logging.warning(f"Slope range does not evenly divide: ending before {m_end}")
    slopes = range(m_start, m_end, m_step)
    logging.info(f"slopes:\n{slopes}")

    if (b_end - b_start) % b_step != 0:
        logging.warning(f"Y-intercept range does not evenly divide: ending before {b_end}")
    y_intercepts = range(b_start, b_end, b_step)
    logging.info(f"y_intercepts:\n{y_intercepts}")

    combinations = list(itertools.product(slopes, y_intercepts))
    logging.info(f"combinations:\n{combinations}")

    if not return_dictionary:
        linear_guesses = combinations
        logging.info("return_dictionary=False, so linear_guesses is list of tuples")
    else:
        linear_guesses = [{'slope': m, 'y_intercept': b} for m, b in combinations]
        logging.info("return_dictionary=True, so linear_guesses is list of dictionaries with keys slope and y_intercept")

    
    logging.info(f"linear_guesses (m,b):\n{json.dumps(linear_guesses, indent=4)}")
    return linear_guesses

# If first data row got saved as header of .csv, this function will fix it
def fix_csv_header(csv_path):
    # Read the CSV file without header
    df = pd.read_csv(csv_path, header=None)

    # Assuming the first row should be the header
    new_header = df.iloc[0]

    # Take the data less the header row
    df = df[1:]

    # Set the new header
    df.columns = new_header

    # Save the fixed DataFrame to a new CSV file
    new_csv_path = csv_path.replace('.csv', '_fixed.csv')
    df.to_csv(new_csv_path, index=False)
    return new_csv_path

# Load a CSV file
def load_csv(filepath, has_header=False):
    with open(filepath, "rt") as file:
        lines = reader(file)
        dataset = list(lines)
        # Skip the first row (header) if has_header is True
        if has_header:
            dataset.pop(0)
    return dataset

# Convert string column to float
def string_column_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())

def get_loggable_json(obj, max_string_length=100, max_list_length=5):
    if isinstance(obj, dict):
        truncated_dict = {}
        for k, v in obj.items():
            if k == 'groups':  # Special handling for 'groups' within 'root'
                truncated_dict[k] = [get_loggable_json(group, max_string_length, max_list_length) for group in v[:max_list_length]]
            elif isinstance(v, list):
                truncated_dict[k] = [get_loggable_json(item, max_string_length, max_list_length) for item in v[:max_list_length]]
            elif isinstance(v, str):
                truncated_dict[k] = v[:max_string_length] + '...' if len(v) > max_string_length else v
            else:
                truncated_dict[k] = v
        return truncated_dict
    elif isinstance(obj, list):
        return [get_loggable_json(item, max_string_length, max_list_length) for item in obj[:max_list_length]]
    elif isinstance(obj, str):
        return obj[:max_string_length] + '...' if len(obj) > max_string_length else obj
    return obj

def initialize_logging(log_path, debug=False):
    # Set base log level
    log_level = logging.DEBUG if debug else logging.INFO

    # Configure the root logger
    logger = logging.getLogger()
    logger.setLevel(log_level)

    # Define the formatter
    console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Check if a console handler already exists
    console_handler_exists = any(isinstance(handler, logging.StreamHandler) for handler in logger.handlers)

    # If a console handler doesn't exist, add one
    if not console_handler_exists:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

    # Ensure log directory exists
    directory_log_path = os.path.dirname(log_path)
    os.makedirs(directory_log_path, exist_ok=True) 

    # Set up file logging
    file_log_level = logging.DEBUG if debug else logging.INFO
    file_handler = logging.FileHandler(log_path, mode='w')
    file_handler.setLevel(file_log_level)
    file_handler.setFormatter(console_formatter)
    logger.addHandler(file_handler)

    logging.info("main(): Debug mode is %s", "ON" if debug else "OFF")