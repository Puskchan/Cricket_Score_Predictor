import sys
import os
import pandas as pd

from src.exception import CustomException
from src.utils import load_obj


class PredictionPipeline:
    def __init__(self) -> None:
        pass

    def predict(self, features):
        try:
            model_path = 'artifacts/model.pkl'
            # preprocessor_path = 'artifacts/preprocessor.pkl'
            model = load_obj(model_path)
            preds = model.predict(features)
            return preds
        
        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(self,
                 Over_Number: int, 
                 Runs_Scored_Till_That_Over: int,
                 Wickets_Taken_Till_That_Over: int, 
                 Runs_in_Last_5_Overs: int, 
                 Wickets_in_Last_5_Overs:int ):
        
        self.Over_Number = Over_Number
        self.Runs_Scored_Till_That_Over = Runs_Scored_Till_That_Over
        self.Wickets_Taken_Till_That_Over = Wickets_Taken_Till_That_Over
        self.Runs_in_Last_5_Overs = Runs_in_Last_5_Overs
        self.Wickets_in_Last_5_Overs = Wickets_in_Last_5_Overs

    def get_data_as_df(self):
        try:
            custom_data_input_dict = {
                'Over_Number' : [self.Over_Number],
                'Runs_Scored_Till_That_Over' : [self.Runs_Scored_Till_That_Over],
                'Wickets_Taken_Till_That_Over' : [self.Wickets_Taken_Till_That_Over],
                'Runs_in_Last_5_Overs' : [self.Runs_in_Last_5_Overs],
                'Wickets_in_Last_5_Overs' : [self.Wickets_in_Last_5_Overs],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e,sys)