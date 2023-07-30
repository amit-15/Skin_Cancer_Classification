from Skin_Cancer_Classification import logger
from Skin_Cancer_Classification.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
import requests

STAGE_NAME = 'Data Ingestion stage'

if __name__ == '__main__':
    try:
        logger.info(f'------------- stage{STAGE_NAME} started -------------')
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f'------------- stage{STAGE_NAME} finished -------------')
    except Exception as e:
        logger.exception(e)
        raise e