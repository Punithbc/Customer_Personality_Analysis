import os


SAVED_MODEL_DIR = os.path.join("saved_models")

#defining common constant variable for training pipeline

TARGET_COLUMN = ""
PIPELINE_NAME = ""
ARTIFACT_DIR = "artifact"
FILE_NAME = "customer.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"
FILTERED_DATA_FILE_NAME = "filter.csv"
SCHEMA_FILE_PATH = os.path.join("config","schema.yaml")

#data ingestion related constants

DATA_INGESTION_DIR_NAME = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR = "feature_store"


#data validation related constants


DATA_VALIDATION_DIR_NAME = "data_validation"
DATA_VALIDATION_DRIFT_REPORT_DIR_NAME = "drift_report"
DATA_VALIDATEION_DRIFT_FILE_NAME = "report.yaml"
DATA_VALIDATION_VALID_DATA_DIR_NAME = "VALID_DATA"
