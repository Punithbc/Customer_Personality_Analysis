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

def save_object(file_path:str, obj:object)-> None:
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
        print("file is saved")    
    except Exception as e:
        raise e


def load_object(file_path:str) -> None:
    try:
        if not os.path.exists(file_path):
            raise Exception(f"The file {file_path} is not exists")
        with open(file_path, 'rb') as file_obj:
            return dill.load(file_obj)    
    except Exception as e:
        raise e        


class wrapper:
    def __init__(self,obj1, obj2):
        self.obj1 = obj1
        self.obj2 = obj2




