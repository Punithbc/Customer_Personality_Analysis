import os


SAVED_MODEL_DIR = os.path.join("saved_models")
PREDICTION_MODEL_FILE_NAME = "final.pkl"

#defining common constant variable for training pipeline
TRAIN_TEST_SPLIT_RATIO: float = 0.2
TARGET_COLUMN = "Clusters"
SEED = 7
TEST_SIZE: float = 0.33
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
 

 #data tranformation part 1 related constants


DATA_TRANSFORMATION_DIR_NAME = "data_transformation_part_1"
DATA_TRANSFORMATION_ENCODED_DIR_NAME = "encoded"
DATA_TRANSFORMATION_ENCODED_DATA_FILE_NAME = "encoded_data.csv"
DATA_TRANSFORMATION_ENCODED_OBJECT_FILE_NAME = "encoded_object.pkl"
DATA_TRANSFORMATION_SCALED__DIR_NAME = "scaled"
DATA_TRANSFORMATION_SCALED_DATA_FILE_NAME = "scaled.csv"
DATA_TRANSFORMATION_SCALED_OBJECT_FILE_NAME = "scaled_object.pkl"



#data transformation part 2 related constants

DATA_TRANSFORMATION_2_DIR_NAME = "data_tranformation_part_2"
DATA_TRANSORMATION_2_PCA_DIR_NAME = "Dimentional_reduction"
DATA_TRANSFORMATION_2_PCA_FILE_NAME = "pca_data.csv"
DATA_TRANSFORMATION_2_PCA_OBJ_FILE_NAME = "pca_obj.pkl"
DATA_TRANSFORMATION_2_CLUSTER_DIR_NAME = "cluster"
DATA_TRANSFORMATION_2_CLUSTER_FILE_NAME = "cluster_data.csv"



#model_trainer related contants

MODEL_TRAINER_DIR_NAME = "model_trainer"
MODEL_TRAINER_TRAIN_TEST_SPLIT_DIR_NAME = "Train_test_split"
MODEL_TRAINER_TRAIN_DATA_FILE_NAME = "train.csv"
MODEL_TRAINER_TEST_DATA_FILE_NAME = "test.csv"
MODEL_TRAINER_MODEL_SAVE_DIR_NAME = "ML_model"
MODEL_TRAINER_MODEL_OBJ_FILE_NAME = "model.pkl"
CONSOLIDATETED_OBJ = "consolidated.pkl"