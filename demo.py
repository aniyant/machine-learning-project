import logging
from housing.config.configuration import Configuration
from housing.pipeline.pipeline import Pipeline

def main():
    try:
        pipeline = Pipeline()
        
        pipeline.run_pipeline()

        #con = Configuration()
        #logging.info(con.get_data_transformation_config())
    except Exception as e:
        logging.error(f"{e}")
        print(0)

if __name__ == "__main__":
    main()