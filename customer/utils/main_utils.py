import yaml
import pandas as pd
import os
import dill
import numpy as np



def read_yaml_file(file_path: str):
    try:
        with open(file_path,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise e


def write_yaml_file(file_path: str, content:object, replace:bool=False):
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path, 'w') as file:
            yaml.dump(content,file)        
    except Exception as e:
        raise e                 