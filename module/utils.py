import logging

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def read_file(filepath):
    with open(filepath, 'r') as f:
        data = f.read()
    return data
