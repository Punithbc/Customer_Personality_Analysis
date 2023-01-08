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
            train_set.to_csv(train_data_file_path)

            #saving test data set

            test_data_file_path = self.model_trainer_config.test_data_file_path
            test_data_dir = os.path.dirname(test_data_file_path)
            os.makedirs(test_data_dir, exist_ok=True)
            test_set.to_csv(test_data_file_path)
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
            random_forest.fit(X_train,y_train)

            #saving ml model
            ml_model_obj_path = self.model_trainer_config.ml_model_obj_file_path
            os.makedirs(os.path.dirname(ml_model_obj_path), exist_ok=True)
            y_train_pred = random_forest.predict(X_train)
            y_test_pred = random_forest.predict(X_test)
            print("training data score")
            train_classfication = get_classification_score(y_true=y_train, y_pred=y_train_pred)
            print("testing data score")
            test_classfication = get_classification_score(y_true=y_test, y_pred=y_test_pred)
            save_object(file_path=ml_model_obj_path, obj=random_forest)
            return [train_classfication,test_classfication]
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
            os.makedirs(os.path.dirname(file_path),exist_ok=True)
            save_object(file_path=file_path, obj=consolidated_obj)
            
        except Exception as e:
            raise e
    



    def initiate_model_trainer(self) -> ModelTrainerArtifact:
        try:
            clustered_dataset = self.data_transformation_artifact_2.clustered_data_file_path
            dataframe = self.read_data(clustered_dataset)
            train_dataframe = self.start_train_test_split(dataframe=dataframe)
            train_classfication, test_classfication = self.train_model(train_dataframe)
            self.creating_consolidated_customerModel()
            model_trainer_artifact = ModelTrainerArtifact(train_metric_artifact=train_classfication, 
            test_metric_artifact=test_classfication,
            consolidated_obj=self.model_trainer_config.consolidated_obj_file_path,
            trained_model_file_path=self.model_trainer_config.ml_model_obj_file_path)
            return model_trainer_artifact
            
        except Exception as e:
            raise e     

