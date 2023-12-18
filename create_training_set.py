import pandas as pd
import os
import logging
import util

create_training_set_log_path = os.path.join("/var", "log", "regression", "create_training_set.log")
util.initialize_logging(create_training_set_log_path)

def pd_to_csv(data, output_path):
    logging.info(f"pd_to_csv(\ndata: {data},\noutput_path: {output_path}\n)")
    df = pd.DataFrame(data)
    df.to_csv(output_path, index=False)
    logging.info(f"Saved data to path: {output_path}")

def main():
    logging.info("main()")
    data = {
        "x": [4, 8, 3, 2, 9],
        "y": [1, 3, 7, 6, 0]
    }

    output_path = os.path.join("training_sets", "data_set_01.csv")
    pd_to_csv(data, output_path)

if __name__ == '__main__':
    main()