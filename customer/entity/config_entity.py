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
        self.dataIngestiondir:str = os.path.join(trainingpipelineconfig.artifact_dir ,training_pipeline.DATA_INGESTION_DIR_NAME)
        self.featureStoreFilePath:str = os.path.join(self.dataIngestiondir,training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR,training_pipeline.FILE_NAME)
        self.collectionName = COLLECTION_NAME


class DataValidationConfig:
    def __init__(self, trainingpipelineconfig: TrainingPipelineConfig):
        self.data_validation_dir: str = os.path.join(trainingpipelineconfig.artifact_dir, training_pipeline.DATA_VALIDATION_DIR_NAME)
        # self.drift_report_dir: str = os.path.join(self.data_validation_dir,training_pipeline.DATA_VALIDATION_DRIFT_REPORT_DIR_NAME)
        # self.drift_report_file_path: str = os.path.join(self.drift_report_dir,training_pipeline.DATA_VALIDATEION_DRIFT_FILE_NAME)        
        self.valid_data_dir: str = os.path.join(self.data_validation_dir,training_pipeline.DATA_VALIDATION_VALID_DATA_DIR_NAME)
        self.filter_data_path: str = os.path.join(self.valid_data_dir, training_pipeline.FILTERED_DATA_FILE_NAME)



