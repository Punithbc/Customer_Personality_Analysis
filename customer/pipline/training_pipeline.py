from customer.components.data_ingestion import DataIngestion
from customer.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig
from customer.entity.artifact_entity import DataIngestionArtifact







class TrainPipeline:
    is_pipeline_running = False
    def __init__(self):
        try:
            self.training_pipline_config = TrainingPipelineConfig()
        except Exception as e:
            raise e     

    def start_data_ingestion(self,data_injestion_config:DataIngestionConfig):
        try:
            injestion_obj = DataIngestion(data_injestion_config=data_injestion_config)
            injestion_artifact  = injestion_obj.initiate_data_injestion()
            return injestion_artifact
        except Exception as e:
            raise e     

    def run_pipeline(self):
        try:
            TrainPipeline.is_pipeline_running = True
            data_injestion_config = DataIngestionConfig(self.training_pipline_config)
            data_injes_arti = self.start_data_ingestion(data_injestion_config=data_injestion_config)
        except Exception as e:
            raise e         



    