from customer.pipline.training_pipeline import TrainPipeline
from customer.pipline.prediction_pipeline import Prediction
import os
import pandas as pd
from fastapi import FastAPI
from uvicorn import run as app_run
from fastapi import Response
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from customer.constant.application import APP_HOST,APP_PORT


app = FastAPI()
origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/predict")
def predict_route():
    try:

        df = pd.read_csv('raw_data.csv').head(5)
        prediction_obj = Prediction(df)
        if not Prediction.is_model_exists():
            return Response("Model is not available")
        result = prediction_obj.start_prediction()
        print("printing the prediciton")
        return Response(result)
    except Exception as e:
        raise e


@app.get("/train")
def train_route():
    try:
        
        training_pipeline = TrainPipeline()
        if TrainPipeline.is_pipeline_running:
            return Response("Training pipeline is already running")
        training_pipeline.run_pipeline()
        return Response("Training successfully")

    except Exception as e:
        raise Response(f"Error Occured {e}")


def main():
    try:
        training_pipeline = TrainPipeline()
        training_pipeline.run_pipeline()

    except Exception as e:
        raise e    

if  __name__ == "__main__":
    main()
    # app_run(app, host=APP_HOST, port=APP_PORT)