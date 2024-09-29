from flask import Flask, request, render_template, redirect, url_for
import numpy as np
import pandas as pd

from src.pipeline.predict_pipeline import CustomData, PredictionPipeline

application = Flask(__name__)

app = application

## Route to homepage

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data = CustomData(
            Over_Number = request.form.get('overNumber'),
            Runs_Scored_Till_That_Over = request.form.get('runsTillOver'),
            Wickets_Taken_Till_That_Over = request.form.get('wicketsTillOver'),
            Runs_in_Last_5_Overs = request.form.get('runsLast5overs'),
            Wickets_in_Last_5_Overs = request.form.get('wicketsLast5overs'),
            Batting_team = request.form.get('battingteam'),
            Bowling_team = request.form.get('bowlingteam'),
        )

        pred_df = data.get_data_as_df()
        
        predict_pipeline = PredictionPipeline()
        results = predict_pipeline.predict(pred_df)

        return render_template('results.html', results=int(results[0]))

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)

# To kill the application you have to close the port while on local machine
# Go to terminal -> Type 'lsof -i :5000' ->
# Then Type 'kill -9 PID' -> Done!
# **Pid will be a number in the starting columns