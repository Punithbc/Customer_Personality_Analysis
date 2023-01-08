from customer.entity.artifact_entity import DataTranformation1Artifact, DataTransformation2Artifat
from customer.entity.config_entity import DataTransformation2Config
import pandas as pd
import os
from sklearn.decomposition import PCA
from sklearn.cluster import AgglomerativeClustering
from customer.utils.main_utils import save_object


class DataTransformation2:
    def __init__(self, data_transformation2config:DataTransformation2Config, data_transformation_1_artifcat: DataTranformation1Artifact):
        try:
            self.data_transformation2config = data_transformation2config
            self.data_transformation_1_artifcat = data_transformation_1_artifcat
        except Exception as e:
            raise e


    @staticmethod
    def read_data(file_path) -> pd.DataFrame:
        try:
            dataframe  = pd.read_csv(file_path)
            return dataframe
        except Exception as e:
            raise e 


    def start_pca(self, dataframe:pd.DataFrame)->pd.DataFrame:
        try:
            pca = PCA(n_components=3)
            pca.fit(dataframe)
            PCA_ds = pd.DataFrame(pca.transform(dataframe), columns=(["col1","col2", "col3"]))
            PCA_ds.describe().T
            #saving pca dataset
            pca_file_path = self.data_transformation2config.pca_file_data_path
            os.makedirs(os.path.dirname(pca_file_path), exist_ok=True)
            PCA_ds.to_csv(pca_file_path, header=True, index=False)
            print("pca dataset saved")
            #saving pca obj file

            pca_obj_path = self.data_transformation2config.pca_obj_path
            os.makedirs(os.path.dirname(pca_obj_path), exist_ok=True)
            save_object(pca_obj_path,obj=pca)
            return PCA_ds
        except Exception as e:
            raise e


    def start_clustering_the_dataset(self, dataframe:pd.DataFrame):
        try:
            #Initiating the Agglomerative Clustering model 
            AC = AgglomerativeClustering(n_clusters=4)
            # fit model and predict clusters
            yhat_AC = AC.fit_predict(dataframe)
            dataframe["Clusters"] = yhat_AC
            #saving cluster data
            cluster_data_path = self.data_transformation2config.cluster_data_file_path
            os.makedirs(os.path.dirname(cluster_data_path))
            dataframe.to_csv(cluster_data_path,header=True, index=False)
            print(f"clusters dataset saved , there are {dataframe['Clusters'].unique()} clusters in total")
        except Exception as e:
            raise e


    def inititate_data_transformation_part_2(self)-> DataTransformation2Artifat:
        try:
            scaled_data_file_path = self.data_transformation_1_artifcat.scaled_data_file_path
            scaled_data = self.read_data(scaled_data_file_path)
            pca_data = self.start_pca(dataframe=scaled_data) 
            self.start_clustering_the_dataset(pca_data)
            data_transformation_2_artifact = DataTransformation2Artifat(clustered_data_file_path=self.data_transformation2config.cluster_data_file_path, 
            pca_obj_path=self.data_transformation2config.pca_obj_path) 
            return data_transformation_2_artifact
        except Exception as e:
            raise e                                