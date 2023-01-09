from customer.pipline.training_pipeline import TrainPipeline
from customer.pipline.prediction_pipeline import Prediction
import os
import pandas as pd




def predicting():
    try:

        df = pd.read_csv('raw_data.csv').head(5)
        prediction_obj = Prediction(df)
        result = prediction_obj.start_prediction()
        print("printing the prediciton")
        print(result)
    except Exception as e:
        raise e



def main():
    try:
        print("main entered")
        training_pipeline = TrainPipeline()
        training_pipeline.run_pipeline()

    except Exception as e:
        raise e


if  __name__ == "__main__":
    predicting()