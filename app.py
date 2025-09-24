from src.exception import CustomException
import sys
from src.logger import logging

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

if __name__ == "__main__":
    # try:
    #     a = 1 / 0
    # except Exception as e:
    #     logging.info("Divide by zero error")
    #     raise CustomException(e, sys)

    #Checking Data ingestion class
    obj_name = DataIngestion()
    train, test = obj_name.initiate_data_ingestion()

    # Checking Data transformation class

    obj_transformation = DataTransformation()
    train_array, test_array, _ = obj_transformation.initiate_data_transformation(train,test)

    # Checking Model trainer class
    obj_model_trainer = ModelTrainer()
    r2_score = obj_model_trainer.initiate_model_trainer(train_array, test_array)
    print(f"The accuracy of the best model is {r2_score}")

    


    



