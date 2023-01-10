import sys
from typing import Optional
import numpy as np
import pandas as pd
import json
from customer.configuration.mongo_db_connection import MongoDBClient
from customer.constant.database import DATABASE_NAME
from customer.logger import logging

class CustomerData:
    '''
    this class helps to export entire mongo db record as pandas dataframe'''
    def __init__(self):
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise e


    def insert_record_to_db(self,file_path, collection_name:str, database_name:Optional[str]=None):
        try:
            dataframe = pd.read_csv(file_path)
            dataframe.reset_index(drop=True, inplace=True)
            records = list(json.loads(dataframe.T.to_json()).values())
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]   
            collection.insert_many(records)
            return len(records)     
        except Exception as e:
            raise e  


    def export_collections_as_dataframe(
        self,collection_name:str, database_name:Optional[str]=None) -> pd.DataFrame:
        try:
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]
            records = collection.find()  
            logging.info("DATASET is collected from database")
            df = pd.DataFrame(list(records))
            print("dataframe created")
            print(df.head())
            if "_id" in df.columns.to_list():
                df = df.drop('_id',axis=1)
            df.replace({"na":np.nan}, inplace= True)
            print(f"len of dataframe {len(df)}")
            return df     
        except Exception  as e:
            raise e 

            