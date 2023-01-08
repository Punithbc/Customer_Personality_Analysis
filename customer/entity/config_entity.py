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


class DataTransformation1Config:
    def __init__(self, training_pipline_config: TrainingPipelineConfig):
        self.data_transformation_1_dir:str = os.path.join(training_pipline_config.artifact_dir, training_pipeline.DATA_TRANSFORMATION_DIR_NAME)
        self.encoded_file_dir: str = os.path.join(self.data_transformation_1_dir, training_pipeline.DATA_TRANSFORMATION_ENCODED_DIR_NAME)
        self.encoded_data_file_path: str = os.path.join(self.encoded_file_dir, training_pipeline.DATA_TRANSFORMATION_ENCODED_DATA_FILE_NAME)
        self.encoded_object_file_path: str = os.path.join(self.encoded_file_dir, training_pipeline.DATA_TRANSFORMATION_ENCODED_OBJECT_FILE_NAME)
        self.scaled_file_dir: str = os.path.join(self.data_transformation_1_dir, training_pipeline.DATA_TRANSFORMATION_SCALED__DIR_NAME)
        self.scaled_data_file_path: str = os.path.join(self.scaled_file_dir, training_pipeline.DATA_TRANSFORMATION_SCALED_DATA_FILE_NAME)
        self.sclaed_object_file_path: str = os.path.join(self.scaled_file_dir, training_pipeline.DATA_TRANSFORMATION_SCALED_OBJECT_FILE_NAME)



class DataTransformation2Config:
    def __init__(self, training_pipline_config:TrainingPipelineConfig):
        self.data_transformation_2_dir:str = os.path.join(training_pipline_config.artifact_dir, training_pipeline.DATA_TRANSFORMATION_2_DIR_NAME)
        self.pca_file_dir: str = os.path.join(self.data_transformation_2_dir, training_pipeline.DATA_TRANSORMATION_2_PCA_DIR_NAME)
        self.pca_file_data_path: str = os.path.join(self.pca_file_dir, training_pipeline.DATA_TRANSFORMATION_2_PCA_FILE_NAME)
        self.pca_obj_path: str = os.path.join(self.pca_file_dir, training_pipeline.DATA_TRANSFORMATION_2_PCA_OBJ_FILE_NAME)
        self.cluster_dir: str = os.path.join(self.data_transformation_2_dir, training_pipeline.DATA_TRANSFORMATION_2_CLUSTER_DIR_NAME)
        self.cluster_data_file_path: str = os.path.join(self.cluster_dir, training_pipeline.DATA_TRANSFORMATION_2_CLUSTER_FILE_NAME)
        


class ModelTrainerConfig:
    def __init__(self, training_pipline_config:TrainingPipelineConfig):
        self.model_trainer_dir: str = os.path.join(training_pipline_config.artifact_dir, training_pipeline.MODEL_TRAINER_DIR_NAME)
        self.train_test_split_dir: str = os.path.join(self.model_trainer_dir, training_pipeline.MODEL_TRAINER_TRAIN_TEST_SPLIT_DIR_NAME)
        self.train_data_file_path: str = os.path.join(self.train_test_split_dir, training_pipeline.MODEL_TRAINER_TRAIN_DATA_FILE_NAME)
        self.test_data_file_path: str = os.path.join(self.train_test_split_dir, training_pipeline.MODEL_TRAINER_TEST_DATA_FILE_NAME)
        self.ml_model_dir: str = os.path.join(self.model_trainer_dir, training_pipeline.MODEL_TRAINER_MODEL_SAVE_DIR_NAME)
        self.ml_model_obj_file_path: str = os.path.join(self.ml_model_dir, training_pipeline.MODEL_TRAINER_MODEL_OBJ_FILE_NAME)

