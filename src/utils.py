import os
import sys
import dill
import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import LabelEncoder


from src.exception import CustomException


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path,'wb') as file_obj:
            dill.dump(obj, file_obj)
        
    except Exception as e:
        raise CustomException(e,sys)
    

class DataPrep(BaseEstimator, TransformerMixin):
    def __init__(self) -> None:
        pass

    def fit(self, X, y=None):
        return self

    def transform(self,df, y=None):
        df['Total Runs'] = None
        df['Total Wickets'] = None

        for i in range(len(df)):
            if(df['Team 1'][i] == df['Batting team'][i]):
                df['Total Runs'][i] = df['Total Score for Team 1'][i]
                df['Total Wickets'][i] = df['Total Wicket for Team 1'][i]
            else:
                df['Total Runs'][i] = df['Total Score for Team 2'][i]
                df['Total Wickets'][i] = df['Total Wicket for Team 2'][i]

        df['Total Runs'] = df['Total Runs'].astype(int)

        df['Runs in Last 5 Overs'] = df['Runs Scored till that over'].diff(periods=5).fillna(0)
        df['Wickets in Last 5 Overs'] = df['Wickets Taken till that over'].diff(periods=5).fillna(0)

        df.drop(['Team 1', 'Team 2', 'Total Score for Team 1', 'Total Score for Team 2', 'Total Wicket for Team 2', 'Total Wicket for Team 1', 'City','Year', 'Match Number', 'Date', 'Winner','Winning Details', 'Match Detail', 'Total Wickets', 'Runs Scored in over', 'Wicket Taken in over'], axis = 1, inplace = True)

        popular_teams = ['ENG', 'NZ', 'PAK', 'NED', 'AFG', 'BAN', 'SA', 'SL', 'AUS', 'IND',
        'WI', 'IRE']
        
        df = df[(df['Batting team'].isin(popular_teams)) & (df['Bowling team'].isin(popular_teams))]

        return df
    


class Encoding(BaseEstimator, TransformerMixin):
    def __init__(self) -> None:
        pass

    def fit(self,X,y=None):
        return self
    
    def transform(self,df, y=None):
        L = LabelEncoder()
        for col in ['Batting team', 'Bowling team']:
            df[col] = L.fit_transform(df[col])

        columns =  ['Over Number', 'Runs Scored till that over',
        'Wickets Taken till that over', 'Total Runs', 'Runs in Last 5 Overs',
        'Wickets in Last 5 Overs', 'Batting team AFG', 'Batting team AUS',
        'Batting team BAN', 'Batting team ENG', 'Batting team IND', 'Batting team IRE',
        'Batting team NED', 'Batting team NZ', 'Batting team PAK', 'Batting team SA',
        'Batting team SL', 'Batting team WI', 'Bowling team AFG',
        'Bowling team AUS', 'Bowling team BAN', 'Bowling team ENG', 'Bowling team IND',
        'Bowling team IRE', 'Bowling team NED', 'Bowling team NZ', 'Bowling team PAK',
        'Bowling team SA', 'Bowling team SL', 'Bowling team WI']
        
        df_encoded = pd.get_dummies(df, columns=['Batting team', 'Bowling team'])

        df_encoded.columns = columns

        return df_encoded
    

def load_obj(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise CustomException(e,sys)
    

def imputation(df):
    try:
        batting =  {'Batting team AFG': [False], 
                    'Batting team AUS': [False],
                    'Batting team BAN': [False], 
                    'Batting team ENG': [False], 
                    'Batting team IND': [False], 
                    'Batting team IRE': [False],
                    'Batting team NED': [False], 
                    'Batting team NZ': [False], 
                    'Batting team PAK': [False], 
                    'Batting team SA': [False],
                    'Batting team SL': [False], 
                    'Batting team WI': [False],} 

        bowling=   {'Bowling team AFG': [False],
                    'Bowling team AUS': [False], 
                    'Bowling team BAN': [False], 
                    'Bowling team ENG': [False], 
                    'Bowling team IND': [False],
                    'Bowling team IRE': [False], 
                    'Bowling team NED': [False], 
                    'Bowling team NZ': [False], 
                    'Bowling team PAK': [False],
                    'Bowling team SA': [False], 
                    'Bowling team SL': [False], 
                    'Bowling team WI': [False],}


        bat = f"Batting team {df['Batting_team'].values[0]}"
        bowl = f"Bowling team {df['Bowling_team'].values[0]}"

        if bat in batting:
            batting[bat] = [True]
        if bowl in bowling:
            bowling[bowl] = [True]

        batting = pd.DataFrame(batting)
        bowling = pd.DataFrame(bowling)

        df = df.drop(['Batting_team','Bowling_team'], axis=1)

        final = pd.concat((df, batting, bowling), axis=1)

        return final
    
    except Exception as e:
        raise CustomException(e,sys)
