import logging
import logging.config
from yaml import safe_load
import os

def logger(name):
    print(f"\nCreating logger {name}.")
    print(os.path.dirname(__file__))
    with open(os.path.join(os.path.dirname(__file__), 'config.yaml'), 'r') as f:
        config = safe_load(f.read())
        logging.config.dictConfig(config)

    return logging.getLogger(name)
