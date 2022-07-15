import logging
from housing.config.configuration import Configuration
from housing.pipeline.pipeline import Pipeline
from housing.constant import CONFIG_DIR, get_current_time_stamp

def main():
    try:
        pipeline = Pipeline()
        
        pipeline.start()

        #con = Configuration()
        #logging.info(con.get_data_transformation_config())
    except Exception as e:
        logging.error(f"{e}")
        print(0)

if __name__ == "__main__":
    main()