from customer.entity.artifact_entity import DataValidationArtifact, DataIngestionArtifact
from customer.entity.config_entity import DataValidationConfig
import pandas as pd
import numpy as np
import yaml
import os
from customer.utils.main_utils import write_yaml_file, read_yaml_file
from customer.constant.training_pipeline import SCHEMA_FILE_PATH
from customer.constant.training_pipeline import FILTERED_DATA_FILE_NAME

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
            print(f"missing columns are{missing_columns}")        
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


    def filling_nan_values(self, dataframe: pd.DataFrame)->pd.DataFrame:
        try:
            income_median = dataframe['Income'].median()
            dataframe.Income.fillna(income_median, inplace=True)
            print(f"no of na values in the dataframe{dataframe.isna().sum()}")
            return dataframe
        except Exception as e:
            raise e    
    

    def merging_some_rows(self, dataframe:pd.DataFrame) -> pd.DataFrame:
        try:
            dataframe["Dt_Customer"] = pd.to_datetime(dataframe["Dt_Customer"])
            dates = []
            for i in dataframe["Dt_Customer"]:
                i = i.date()
                dates.append(i)
            #Dates of the newest and oldest recorded customer
            print("The newest customer's enrolment date in therecords:",max(dates))
            print("The oldest customer's enrolment date in the records:",min(dates))
            #Created a feature "Customer_For"
            days = []
            d1 = max(dates) #taking it to be the newest customer
            for i in dates:
                delta = d1 - i
                days.append(delta)
            dataframe["Customer_For"] = days
            dataframe["Customer_For"] = pd.to_numeric(dataframe["Customer_For"], errors="coerce")
            #Feature Engineering
            #Age of customer today 
            dataframe["Age"] = 2021-dataframe["Year_Birth"]

            #Total spendings on various items
            dataframe["Spent"] = dataframe["MntWines"]+ dataframe["MntFruits"]+ dataframe["MntMeatProducts"]+ dataframe["MntFishProducts"]+ dataframe["MntSweetProducts"]+ dataframe["MntGoldProds"]

            #Deriving living situation by marital status"Alone"
            dataframe["Living_With"]=dataframe["Marital_Status"].replace({"Married":"Partner", "Together":"Partner", "Absurd":"Alone", "Widow":"Alone", "YOLO":"Alone", "Divorced":"Alone", "Single":"Alone",})

            #Feature indicating total children living in the household
            dataframe["Children"]=dataframe["Kidhome"]+dataframe["Teenhome"]

            #Feature for total members in the householde
            dataframe["Family_Size"] = dataframe["Living_With"].replace({"Alone": 1, "Partner":2})+ dataframe["Children"]

            #Feature pertaining parenthood
            dataframe["Is_Parent"] = np.where(dataframe.Children> 0, 1, 0)

            #Segmenting education levels in three groups
            dataframe["Education"]=dataframe["Education"].replace({"Basic":"Undergraduate","2n Cycle":"Undergraduate", "Graduation":"Graduate", "Master":"Postgraduate", "PhD":"Postgraduate"})

            #For clarity
            dataframe=dataframe.rename(columns={"MntWines": "Wines","MntFruits":"Fruits","MntMeatProducts":"Meat","MntFishProducts":"Fish","MntSweetProducts":"Sweets","MntGoldProds":"Gold"})

            #Dropping some of the redundant features
            to_drop = ["Marital_Status", "Dt_Customer", "Z_CostContact", "Z_Revenue", "Year_Birth", "ID"]
            dataframe = dataframe.drop(to_drop, axis=1)
            dataframe = dataframe[(dataframe["Age"]<90)]
            dataframe = dataframe[(dataframe["Income"]<600000)]
            print("The total number of data-points after removing the outliers are:", len(dataframe))
            print(dataframe.describe())
            return dataframe
        except Exception as e:
            raise e    
    
    
    def initiate_data_validation(self)->DataValidationArtifact:
        try:
            file_path = self.data_injection_artifact.featureStorePath
            dataframe = self.read_data(file_path=file_path)
            filepath = os.path.dirname(self.data_validation_config.filter_data_path)
            print(f"filter data path {filepath}")
            is_validated = True 
            os.makedirs(filepath,exist_ok=True)
            if self.validate_number_of_columns(dataframe) and self.is_numerical_column_exists(dataframe):
                dataframe_filled_nan = self.filling_nan_values(dataframe)
                filtered_data_frame = self.merging_some_rows(dataframe_filled_nan)
                filtered_data_frame.to_csv(self.data_validation_config.filter_data_path,index=False, header=True)
                print("filterd data is been saved")
                
            else:
                print("validation was failed")
                is_validated = False
            datavalidationartifcat = DataValidationArtifact(validation_status=is_validated, filtered_data_file_path=filepath)
            return datavalidationartifcat        
        except Exception as e:
            raise e        
