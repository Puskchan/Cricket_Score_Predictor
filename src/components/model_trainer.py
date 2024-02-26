import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dataclasses import dataclass

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

from src.utils import save_object
from src.logger import logging
from src.exception import CustomException


@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")

class ModelTrainer:
    def __init__(self) -> None:
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_arr, test_arr, preprocessor_path=None):
        try:
            logging.info("Split train and test")
            X_train, y_train, X_test, y_test=(
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]
            )

            model = RandomForestRegressor(max_depth=36)
            model.fit(X_train, y_train)
            logging.info("Model selected for use and fitted on the data.")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=model
            )

            logging.info("Model pickle file saved.")

            y_pred = model.predict(X_test)
            score = r2_score(y_test, y_pred)*100
            return score



        except Exception as e:
            CustomException(e,sys)