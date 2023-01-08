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
    # encoded_object_file_path:str
    scaled_data_file_path:str
    # scaled_data_object_path:str


@dataclass
class DataTransformation2Artifat:
    clustered_data_file_path: str    
          
    