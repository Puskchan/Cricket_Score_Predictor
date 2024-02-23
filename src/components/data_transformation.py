import sys
import os
from dataclasses import dataclass
import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object
from src.utils import DataPrep
from src.utils import Encoding


@dataclass
class DataTransformationConfig:
    preprocessor_ob_path = os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self) -> None:
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        try:
            features = ['Year', 
                                  'Total Score for Team 1', 
                                  'Total Wicket for Team 1', 
                                  'Total Score for Team 2', 
                                  'Total Wicket for Team 2', 
                                  'Over Number', 
                                  'Runs Scored in over', 
                                  'Runs Scored till that over', 
                                  'Wicket Taken in over', 
                                  'Wickets Taken till that over',
                                  'Match Number', 
                                  'City', 
                                  'Date', 
                                  'Winner', 
                                  'Team 1', 
                                  'Team 2', 
                                  'Batting team', 
                                  'Bowling team', 
                                  'Winning Details', 
                                  'Match Detail']
            
            pipeline = Pipeline(
                steps=[
                    ('prep',DataPrep()),
                    ('encoder',Encoding())
                ]
            )

            logging.info(f'Columns in pipeline : {features}')

            preprocessor = ColumnTransformer(
                [
                    ('pipe', pipeline, features),
                ]
            )

            return preprocessor

             
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path, test_path):

        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info('Read Train and Test data')

            logging.info('Obtaining preprocessing object')

            preprocessing_obj = self.get_data_transformer_object()

            inp_train_arr = pd.DataFrame(preprocessing_obj.fit_transform(train_df))
            inp_test_arr = pd.DataFrame(preprocessing_obj.fit_transform(test_df))


            target_column_name = 3


            inp_feature_train_df = inp_train_arr.drop(columns=[target_column_name],axis=1)
            target_feature_train_df = inp_train_arr[target_column_name]

            inp_feature_test_df = inp_test_arr.drop(columns=[target_column_name],axis=1)
            target_feature_test_df = inp_test_arr[target_column_name]

            logging.info('Applying preprocessing object on training and testing dataframe.')

            


            train_arr = np.c_[inp_feature_train_df, np.array(target_feature_train_df)]
            test_arr = np.c_[inp_feature_test_df, np.array(target_feature_test_df)]

            save_object(
                file_path=self.data_transformation_config.preprocessor_ob_path,
                obj=preprocessing_obj
            )

            logging.info(f'Saved preprocessing object')

            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_ob_path,
            )

        except Exception as e:
            raise CustomException(e,sys)