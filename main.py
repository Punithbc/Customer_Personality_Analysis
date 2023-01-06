from customer.pipline.training_pipeline import TrainPipeline





def main():
    try:
        print("main entered")
        training_pipeline = TrainPipeline()
        training_pipeline.run_pipeline()

    except Exception as e:
        raise e


if  __name__ == "__main__":
    main()           