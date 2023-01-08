from customer.entity.artifact_entity import DataValidationArtifact, DataTranformation1Artifact
from customer.entity.config_entity import DataTransformation1Config
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder 
import os
from customer.utils.main_utils import save_object
class DataTransformation1:
    def __init__(self, data_tansformation_config1: DataTransformation1Config, data_validation_artifact: DataValidationArtifact):
        try:
            self.data_tansformation_config1 = data_tansformation_config1
            self.data_validation_artifact = data_validation_artifact
        except Exception as e:
            raise e
    
    
    @staticmethod
    def read_data(file_path) -> pd.DataFrame:
        try:
            dataframe  = pd.read_csv(file_path)
            return dataframe
        except Exception as e:
            raise e   

    def encoding_the_filtered_dataset(self) -> pd.DataFrame:
        try:
            file_path_filtered = self.data_validation_artifact.filtered_data_file_path
            df = self.read_data(file_path_filtered)
            #Get list of categorical variables
            s = (df.dtypes == 'object')
            object_cols = list(s[s].index)

            print("Categorical variables in the dataset:", object_cols)

            LE=LabelEncoder()
            for i in object_cols:
                df[i]=df[[i]].apply(LE.fit_transform)
                
            print("All features are now numerical")

            #saving the encoded dataset
            saving_file_path = self.data_tansformation_config1.encoded_data_file_path
            os.makedirs(os.path.dirname(saving_file_path), exist_ok= True)
            df.to_csv(saving_file_path, header=True , index=False)
            #saving the encoded object
            encoded_obj_file_path = self.data_tansformation_config1.encoded_object_file_path

            save_object(encoded_obj_file_path, LE)
            return df
        except Exception as e:
            raise e    



    def scaling_the_encoded_dataset(self, dataframe: pd.DataFrame):
        try:
            dataframe = dataframe.dropna()
            scaler = StandardScaler()
            scaler.fit(dataframe)
            scaled_ds = pd.DataFrame(scaler.transform(dataframe),columns= dataframe.columns)
            print("All features are now scaled")

            #saving the scaled dataset
            saving_file_path = self.data_tansformation_config1.scaled_data_file_path
            os.makedirs(os.path.dirname(saving_file_path), exist_ok=True)
            scaled_ds.to_csv(saving_file_path, header=True, index=False)
            #saving the scaled obj


            scaled_obj_file_path = self.data_tansformation_config1.sclaed_object_file_path
            save_object(scaled_obj_file_path, scaler)
        except Exception as e:
            raise e            


    def initiate_data_transformation_1(self)->DataTranformation1Artifact:
        try:
            scaled_data_file = self.data_tansformation_config1.scaled_data_file_path
            encoded_df = self.encoding_the_filtered_dataset()
            self.scaling_the_encoded_dataset(encoded_df)
            datatransformation_artifact = DataTranformation1Artifact(scaled_data_file_path=scaled_data_file,
            scaled_data_object_path=self.data_tansformation_config1.sclaed_object_file_path, encoded_object_file_path=self.data_tansformation_config1.encoded_object_file_path)
            return datatransformation_artifact
        except Exception as e:
            raise e
