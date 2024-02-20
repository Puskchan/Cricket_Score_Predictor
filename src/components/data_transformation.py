import sys
import os
from dataclasses import dataclass
import numpy as np
import pandas as pd

from src.utils import save_object

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.preprocessing import LabelEncoder

from src.exception import CustomException
from src.logger import logging


@dataclass
class DataTransformationConfig:
    preprocessor_ob_path = os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self) -> None:
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        try:
            numerical_features = ['Year', 
                                  'Total Score for Team 1', 
                                  'Total Wicket for Team 1', 
                                  'Total Score for Team 2', 
                                  'Total Wicket for Team 2', 
                                  'Over Number', 
                                  'Runs Scored in over', 
                                  'Runs Scored till that over', 
                                  'Wicket Taken in over', 
                                  'Wickets Taken till that over']
            
            categorical_features = ['Match Number', 
                                    'City', 
                                    'Date', 
                                    'Winner', 
                                    'Team 1', 
                                    'Team 2', 
                                    'Batting team', 
                                    'Bowling team', 
                                    'Winning Details', 
                                    'Match Detail']
            
            num_pipeline = Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='median')),
                    ('scaler',StandardScaler())
                ]
            )

            logging.info(f'Numerical columns in pipeline : {numerical_features}')

            cat_pipeline=Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('encoder',LabelEncoder())
                ]
            )

            
            logging.info(f'Categorical columns in pipeline : {categorical_features}')

            preprocessor = ColumnTransformer(
                [
                    ('num_pipe', num_pipeline, numerical_features),
                    ('cat_pipe', cat_pipeline, categorical_features)
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

            target_column_name = ''
            numerical_columns = ['']

            inp_feature_train_df = train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df = train_df[target_column_name]

            inp_feature_test_df = test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df = test_df[target_column_name]

            logging.info('Applying preprocessing object on training and testing dataframe.')

            inp_train_arr = preprocessing_obj.fit_transform(inp_feature_train_df)
            inp_test_arr = preprocessing_obj.fit_transform(inp_feature_test_df)

            train_arr = np.c_[inp_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[inp_test_arr, np.array(target_feature_test_df)]

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