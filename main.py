from CnnClassifier import logger
from CnnClassifier.pipelinie.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME= "Data Ingestion stage"



try:
    logger.info(f">>>>>>>>>> {STAGE_NAME} started <<<<<<<")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>> {STAGE_NAME} completed <<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
     
