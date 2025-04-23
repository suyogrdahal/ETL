import logging
import os

def setup_logging(log_file='logs/etl_pipeline.log'):
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()  # also prints to console
        ]
    )
