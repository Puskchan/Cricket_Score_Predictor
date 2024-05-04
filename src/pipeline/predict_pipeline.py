import sys
import pandas as pd

from src.exception import CustomException
from src.utils import load_obj
from src.utils import imputation


class PredictionPipeline:
    def __init__(self) -> None:
        pass

    def predict(self, features):
        try:
            model_path = 'artifacts/model.pkl'
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
                 Wickets_in_Last_5_Overs:int,
                 Batting_team:int,
                 Bowling_team:int ):
        
        self.Over_Number = Over_Number
        self.Runs_Scored_Till_That_Over = Runs_Scored_Till_That_Over
        self.Wickets_Taken_Till_That_Over = Wickets_Taken_Till_That_Over
        self.Runs_in_Last_5_Overs = Runs_in_Last_5_Overs
        self.Wickets_in_Last_5_Overs = Wickets_in_Last_5_Overs
        self.Batting_team = Batting_team
        self.Bowling_team = Bowling_team

    def get_data_as_df(self):
        try:
            custom_data_input_dict = {
                'Over_Number' : [self.Over_Number],
                'Runs_Scored_Till_That_Over' : [self.Runs_Scored_Till_That_Over],
                'Wickets_Taken_Till_That_Over' : [self.Wickets_Taken_Till_That_Over],
                'Runs_in_Last_5_Overs' : [self.Runs_in_Last_5_Overs],
                'Wickets_in_Last_5_Overs' : [self.Wickets_in_Last_5_Overs],
                'Batting_team' : [self.Batting_team],
                'Bowling_team' : [self.Bowling_team]
            }

            temp = imputation(pd.DataFrame(custom_data_input_dict))
            
            return temp

        except Exception as e:
            raise CustomException(e,sys)