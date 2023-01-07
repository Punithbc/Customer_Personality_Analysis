from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:
    featureStorePath:str


@dataclass
class DataValidationArtifact:
    validation_status: bool
    # drift_report_file_path: str
    filtered_data_file_path: str    
    