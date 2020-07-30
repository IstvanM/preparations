import os
import configparser
from functools import lru_cache

@lru_cache(maxsize=256)
def get_config(section: str, conf: str):
    env = os.getenv('environment')
    if env != 'prod':
        env='dev'
    config = configparser.ConfigParser()
    config.read(f'config/{env}.ini')
    res = config[section][conf]
    print(f'{env}: {section}/{conf}={res}')
    return res
