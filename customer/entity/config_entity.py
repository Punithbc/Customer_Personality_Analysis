from datetime import datetime
import os
from customer.constant import training_pipeline
from customer.constant.database import COLLECTION_NAME




class TrainingPipelineConfig:
    def __init__(self,timestamp=datetime.now()):
        timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.artifact_dir = os.path.join(training_pipeline.ARTIFACT_DIR, timestamp)
        self.timestamp:str = timestamp


class DataIngestionConfig:
    def __init__(self, trainingpipelineconfig: TrainingPipelineConfig):
        self.dataIngestiondir:str = os.path.join(TrainingPipelineConfig().artifact_dir ,training_pipeline.DATA_INGESTION_DIR_NAME)
        self.featureStoreFilePath:str = os.path.join(self.dataIngestiondir,training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR,training_pipeline.FILE_NAME)
        self.collectionName = COLLECTION_NAME


