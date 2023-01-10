from customer.components.data_validation import DataValidation
import pandas as pd
import re, os
from customer.constant.training_pipeline import SAVED_MODEL_DIR, PREDICTION_MODEL_FILE_NAME
from customer.utils.main_utils import load_object
class Prediction:
    def __init__(self,dataframe:pd.DataFrame):
        try:
            self.data_frame = dataframe
        except Exception as e:
            raise e

    def start_feature_filtering(self,dataframe:pd.DataFrame)-> pd.DataFrame:
        income_median = dataframe['Income'].median()
        dataframe.Income.fillna(income_median, inplace=True)
        fileterd_dataframe:pd.DataFrame = DataValidation.merging_some_rows(dataframe=dataframe)
        filered_dataframe = fileterd_dataframe.dropna()
        return filered_dataframe


    @classmethod
    def find_latest_model(cls):
        try:
            path = os.path.join(SAVED_MODEL_DIR)
            latest_model_time_stamp = max(list(map(int,os.listdir(path))))
            latest_model_path = os.path.join(SAVED_MODEL_DIR,f"{latest_model_time_stamp}",PREDICTION_MODEL_FILE_NAME)
            print(f"latest model path == {latest_model_path}")
            return latest_model_path
        except Exception as e:
            raise e
    

    def is_model_exists(cls)->bool:
        try:
            if not os.path.exists(SAVED_MODEL_DIR):
                return False

            timestamps = os.listdir(SAVED_MODEL_DIR)
            if len(timestamps)==0:
                return False

            latest_model_path = Prediction.find_latest_model()  

            if not os.path.exists(latest_model_path):
                return False

            return True           

        except Exception as e:
            raise e        


    def start_prediction(self)->pd.DataFrame:
        try:
            dataframe = self.data_frame
            filtered_dataframe = self.start_feature_filtering(dataframe=dataframe)
            latest_model_path = self.find_latest_model()
            model = load_object(file_path=latest_model_path)
            y_hat = model.predict(filtered_dataframe)
            return y_hat
        except Exception as e:
            raise e


            
