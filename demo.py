import logging
from housing.pipeline.pipeline import Pipeline

def main():
    try:
        pipeline = Pipeline()
        
        pipeline.run_pipeline()
    except Exception as e:
        logging.error(f"{e}")
        print(0)

if __name__ == "__main__":
    main()