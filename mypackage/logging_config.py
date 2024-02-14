import os
import logging

def configure_logging(log_file_path='kata09-checkout.log'):
    log_level = os.environ.get('LOG_LEVEL', 'INFO')
    numeric_log_level = getattr(logging, log_level.upper(), None)
    if not isinstance(numeric_log_level, int):
        logging.basicConfig(level=logging.ERROR)

    logging.basicConfig(level=numeric_log_level, format='%(asctime)s - %(levelname)s - %(message)s')

    # Create a FileHandler to output logs to a file
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logging.getLogger().addHandler(file_handler)

# Configure logging when the module is imported
configure_logging()
