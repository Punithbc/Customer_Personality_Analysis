from customer.entity.artifact_entity import DataIngestionArtifact
from customer.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig
from customer.data_access.Customer_data import CustomerData
from customer.constant.database import DATABASE_NAME
import os

class DataIngestion:
    def __init__(self, data_injestion_config: DataIngestionConfig):
        try:
            self.data_injestion_config = data_injestion_config(TrainingPipelineConfig)
            self.collection_name = self.data_injestion_config.collectionName
        except Exception as e:
            raise e    

    def export_data_to_feature_store(self):
        try:
            customer_data_obj = CustomerData()
            dataframe = customer_data_obj.export_collections_as_dataframe(collection_name=self.collection_name)
            feature_Store_path = self.data_injestion_config.featureStoreFilePath
            dirpath = os.path.dirname(feature_Store_path)
            os.makedirs(dirpath,exist_ok=True)
            dataframe.to_csv(feature_Store_path,index=False,header=True)
            return dataframe
        except Exception as e:
            raise e    

    def initiate_data_injestion(self) -> DataIngestionArtifact:
        try:
            dataframe = self.export_data_to_feature_store()
            data_injestion_artifact = DataIngestionArtifact(featureStorePath=self.data_injestion_config.featureStoreFilePath)
            return data_injestion_artifact
        except Exception as e:
            raise e


