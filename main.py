from Skin_Cancer_Classification import logger
from Skin_Cancer_Classification.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from Skin_Cancer_Classification.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
import requests

STAGE_NAME = 'Prepare base model'

if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        prepare_base_model = PrepareBaseModelTrainingPipeline()
        prepare_base_model.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e