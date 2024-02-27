from flask import Flask,request,render_template
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
            Over_Number = request.form.get('Over_Number'),
            Runs_Scored_Till_That_Over = request.form.get('Runs_Scored_Till_That_Over'),
            Wickets_Taken_Till_That_Over = request.form.get('Wickets_Taken_Till_That_Over'),
            Runs_in_Last_5_Overs = request.form.get('Runs_in_Last_5_Overs'),
            Wickets_in_Last_5_Overs = request.form.get('Wickets_in_Last_5_Overs'),
        )

        pred_df = data.get_data_as_df()

        # add the imputer and fix that batting and bowling thing
        # just fill in the teams playing to true and 
        # then fill rest with false
        
        predict_pipeline = PredictionPipeline()
        results = predict_pipeline.predict(pred_df)

        return render_template('home.html', results=results[0])
    

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)