from customer.utils.main_utils import save_object,load_object
from customer.entity.artifact_entity import DataTranformation1Artifact, DataTransformation2Artifat, ModelTrainerArtifact
from customer.entity.config_entity import ModelTrainerConfig
import os, sys
from sklearn.ensemble import RandomForestClassifier
from customer.ml.metric.classification_metric import get_classification_score
import pandas as pd
from sklearn.model_selection import train_test_split
from customer.constant.training_pipeline import SEED, TEST_SIZE, TARGET_COLUMN, TRAIN_TEST_SPLIT_RATIO
from customer.ml.model.estimator import CustomerModel
import time 
from sklearn.metrics import accuracy_score
from customer.constant.training_pipeline import SAVED_MODEL_DIR, PREDICTION_MODEL_FILE_NAME
from customer.logger import logging

class ModelTrainer:
    def __init__(self,model_trainer_config:ModelTrainerConfig, 
        data_tranformation_artifact_1:DataTranformation1Artifact,
        data_transformation_artifact_2:DataTransformation2Artifat):
        try:
            self.model_trainer_config = model_trainer_config
            self.data_tranformation_artifact_1 = data_tranformation_artifact_1
            self.data_transformation_artifact_2 = data_transformation_artifact_2
        except Exception as e:
            raise e


    def start_train_test_split(self, dataframe:pd.DataFrame) -> pd.DataFrame:
        try: 
            train_set, test_set = train_test_split(dataframe, train_size=TRAIN_TEST_SPLIT_RATIO, random_state=SEED)
            print("train and test data splitted")

            #saving train data set
            train_data_file_path = self.model_trainer_config.train_data_file_path
            train_data_dir = os.path.dirname(train_data_file_path)
            os.makedirs(train_data_dir, exist_ok=True)
            train_set.to_csv(train_data_file_path, header=True, index=False)

            #saving test data set

            test_data_file_path = self.model_trainer_config.test_data_file_path
            test_data_dir = os.path.dirname(test_data_file_path)
            os.makedirs(test_data_dir, exist_ok=True)
            test_set.to_csv(test_data_file_path, header=True, index=False)
            return train_set

            

        except Exception as e:
            raise e

    @staticmethod
    def read_data(file_path) -> pd.DataFrame:
        try:
            dataframe  = pd.read_csv(file_path)
            return dataframe
        except Exception as e:
            raise e 

    def train_model(self, dataframe:pd.DataFrame):
        try:
            X = dataframe.drop(TARGET_COLUMN, axis=1)
            Y = dataframe[TARGET_COLUMN]
            X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=TEST_SIZE, random_state=SEED)
            random_forest = RandomForestClassifier()
            print(X_train.head(10))
            print(y_train.head(10))
            random_forest.fit(X_train,y_train)
            logging.info("Training has begun")
            time.sleep(2)
            #saving ml model
            ml_model_obj_path = self.model_trainer_config.ml_model_obj_file_path
            os.makedirs(os.path.dirname(ml_model_obj_path), exist_ok=True)
            y_train_pred = random_forest.predict(X_train)
            y_test_pred = random_forest.predict(X_test)
            clusters_list = dataframe[TARGET_COLUMN].unique()
            total_no_clusters = len(clusters_list)
            final_result = f'''there are {total_no_clusters} clusters found in this dataset after PCA and clustering. 
            {clusters_list} are the clusters.Model's been trained with clusters. Accuracy score is {accuracy_score(y_true=y_train, y_pred=y_train_pred)*100}'''
            logging.info(final_result)
            print(f"accuracy score is {accuracy_score(y_true=y_train, y_pred=y_train_pred)*100}")
            logging.info(f"accuracy score is {accuracy_score(y_true=y_train, y_pred=y_train_pred)*100}")
            print("training data score")
            # train_classfication = get_classification_score(y_true=y_train, y_pred=y_train_pred)
            train_classfication = ""
            print("testing data score")
            # test_classfication = get_classification_score(y_true=y_test, y_pred=y_test_pred)
            test_classfication=""
            save_object(file_path=ml_model_obj_path, obj=random_forest)
            logging.info(f"saving the ML model in {ml_model_obj_path} ")
            return final_result
        except Exception as e:
            raise e

    def creating_consolidated_customerModel(self):
        try:
            encoded_obj = load_object(self.data_tranformation_artifact_1.encoded_object_file_path)
            scaled_obj = load_object(self.data_tranformation_artifact_1.scaled_data_object_path)
            pca_obj = load_object(self.data_transformation_artifact_2.pca_obj_path)
            ml_obj = load_object(self.model_trainer_config.ml_model_obj_file_path)
            consolidated_obj = CustomerModel(encoder_obj=encoded_obj,scaled_obj=scaled_obj, pca_obj=pca_obj, model_obj=ml_obj)
            #saving consolitdate_obj

            file_path  = self.model_trainer_config.consolidated_obj_file_path
            logging.info(f"Saving all objects as consolidated objects in {file_path}")
            logging.info("consolidated object constitues encoded, scaled, pca and ML model")
            os.makedirs(os.path.dirname(file_path),exist_ok=True)
            save_object(file_path=file_path, obj=consolidated_obj)
            timestamp_for_path = self.model_trainer_config.training_pipline_config.timestamp1
                                
            saving_file_path = os.path.join(SAVED_MODEL_DIR,str(timestamp_for_path),PREDICTION_MODEL_FILE_NAME)
            os.makedirs(os.path.dirname(saving_file_path),exist_ok=True)
            save_object(file_path=saving_file_path,obj=consolidated_obj)
            
        except Exception as e:
            raise e
    



    def initiate_model_trainer(self) -> ModelTrainerArtifact:
        try:
            clustered_dataset = self.data_transformation_artifact_2.clustered_data_file_path
            dataframe = self.read_data(clustered_dataset)
            logging.info("reading the clustered dataset and starting the split the data")
            train_dataframe = self.start_train_test_split(dataframe=dataframe)
            final_result = self.train_model(train_dataframe)
            self.creating_consolidated_customerModel()
            model_trainer_artifact = ModelTrainerArtifact(train_metric_artifact="None", 
            test_metric_artifact="None",
            consolidated_obj=self.model_trainer_config.consolidated_obj_file_path,
            trained_model_file_path=self.model_trainer_config.ml_model_obj_file_path)
            return final_result
            
        except Exception as e:
            raise e     

