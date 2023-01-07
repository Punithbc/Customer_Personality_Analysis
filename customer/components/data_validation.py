from customer.entity.artifact_entity import DataValidationArtifact, DataIngestionArtifact
from customer.entity.config_entity import DataValidationConfig
import pandas as pd
import numpy as np
import yaml
from customer.utils.main_utils import write_yaml_file, read_yaml_file
from customer.constant.training_pipeline import SCHEMA_FILE_PATH

class DataValidation:
    def __init__(self, data_injection_artifact:DataIngestionArtifact, data_validation_config:DataValidationConfig):
        try:
            self.data_injection_artifact = data_injection_artifact
            self.data_validation_config = data_validation_config
            self._schema_file = read_yaml_file(SCHEMA_FILE_PATH)

        except Exception as e:
            raise e

    def validate_number_of_columns(self, dataframe: pd.DataFrame) -> bool:
        try:
            print("validating number of columns")
            ymal_data = self._schema_file
            if len(ymal_data["columns"]) == len(dataframe.columns):
                print("validation number of columns successfull")
                return True
            else:
                return False
        except Exception as e:
            raise e            


    def is_numerical_column_exists(self, dataframe: pd.DataFrame) -> bool:
        try:
            numerical_columns = [column for column in dataframe.columns if dataframe[column].dtypes!='O']
            ymal_data = self._schema_file
            numerical_columns_ymal = list(ymal_data['numerical_columns'].keys())
            is_numerical_column_present = True
            missing_columns = []
            for column in numerical_columns:
                if column not in numerical_columns_ymal:
                    is_numerical_column_exist = False
                    missing_columns.append(column)
            print(f"missing columns are"{missing_columns})        
            return is_numerical_column_present        

        except Exception as e:
            raise e

    @staticmethod
    def read_data(file_path) -> pd.DataFrame:
        try:
            dataframe  = pd.read_csv(file_path)
            return dataframe
        except Exception as e:
            raise e    


    def filling_nan_values():...
    

    def merging_some_rows():...
    
    
    def initiate_data_validation():...
