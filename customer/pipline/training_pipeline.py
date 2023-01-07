from customer.components.data_ingestion import DataIngestion
from customer.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig, DataValidationConfig
from customer.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
from customer.components.data_validation import DataValidation







class TrainPipeline:
    is_pipeline_running = False
    def __init__(self):
        try:
            self.training_pipline_config = TrainingPipelineConfig()
        except Exception as e:
            raise e     

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_injestion_config = DataIngestionConfig(trainingpipelineconfig=self.training_pipline_config)
            injestion_obj = DataIngestion(data_injestion_config=data_injestion_config)
            injestion_artifact  = injestion_obj.initiate_data_injestion()
            return injestion_artifact
        except Exception as e:
            raise e


    def start_data_validation(self,data_injestion_artifact:DataIngestionArtifact) -> DataValidationArtifact:
        try:
            data_validation_config = DataValidationConfig(trainingpipelineconfig=self.training_pipline_config)
            data_validation_obj = DataValidation(data_injection_artifact=data_injestion_artifact, data_validation_config=data_validation_config)
            data_validation_artifact = data_validation_obj.initiate_data_validation()
            return data_validation_artifact

        except Exception as e:
            raise e            

    def run_pipeline(self):
        try:
            TrainPipeline.is_pipeline_running = True
            data_injestion_config = DataIngestionConfig(self.training_pipline_config)
            data_injes_arti = self.start_data_ingestion()
            data_valid_arti = self.start_data_validation(data_injestion_artifact=data_injes_arti)
        except Exception as e:
            raise e         



    