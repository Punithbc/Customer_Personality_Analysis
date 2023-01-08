from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:
    featureStorePath:str


@dataclass
class DataValidationArtifact:
    validation_status: bool
    # drift_report_file_path: str
    filtered_data_file_path: str  

@dataclass
class DataTranformation1Artifact:
    # encoded_data_file_path:str
    encoded_object_file_path:str
    scaled_data_file_path:str
    scaled_data_object_path:str


@dataclass
class DataTransformation2Artifat:
    clustered_data_file_path: str
    pca_obj_path: str    
          
@dataclass  
class ClassificationMetricArtifact:
    f1_score: float
    precision_score: float
    recall_score: float

@dataclass
class ModelTrainerArtifact:
    trained_model_file_path:str
    train_metric_artifact: ClassificationMetricArtifact
    test_metric_artifact: ClassificationMetricArtifact  
    consolidated_obj : str 

