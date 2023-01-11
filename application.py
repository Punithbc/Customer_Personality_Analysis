from customer.pipline.training_pipeline import TrainPipeline
from customer.pipline.prediction_pipeline import Prediction
import os
import pandas as pd
from customer.constant.application import APP_HOST,APP_PORT
from flask import Flask, render_template, request


application = Flask(__name__)

@application.route('/',methods=['GET','POST'])
def home_page():
    return render_template('index.html')






@application.route('/predict',methods=['GET','POST'])
def predict_route():
    try:

        df = pd.read_csv('raw_data.csv').head(5)
        prediction_obj = Prediction(df)
        if not Prediction.is_model_exists():
            return "Model is not available"
        result = prediction_obj.start_prediction()
        print("printing the prediciton")
        return render_template('result.html', data=result)
    except Exception as e:
        raise e


@application.route('/train',methods=['GET','POST'])
def train_route():
    try:
        
        training_pipeline = TrainPipeline()
        if TrainPipeline.is_pipeline_running:
            return "Training pipeline is already running"
        result = training_pipeline.run_pipeline()
        return render_template('result.html', data=result)

    except Exception as e:
        raise f"Error Occured {e}"


# def main():
#     try:
#         training_pipeline = TrainPipeline()
#         result = training_pipeline.run_pipeline()
#         print(result)

#     except Exception as e:
#         raise e    

if  __name__ == "__main__":
    application.run(debug=True, port=APP_PORT,host=APP_HOST)
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(asyncio.wait(app_run(app)))
    # app_run(app, host=APP_HOST, port=APP_PORT)