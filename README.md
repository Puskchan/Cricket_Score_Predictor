
# Cricket Score Predictor

The Cricket Score Predictor is an MLOps-driven application designed to predict the final score of a cricket team during a match based on real-time parameters. I developed this project using Python, Flask, and Docker to ensure it is both lightweight and scalable. The core of the system uses historical match data to make accurate predictions, with a model achieving 77% prediction accuracy.

The application is built with custom exception handling and logging to improve reliability and debugging efficiency. I deployed it on AWS and Azure to ensure seamless access and scalability in different environments. This project showcases the power of machine learning in sports analytics and highlights my expertise in building robust, cloud-deployed ML applications.

I also wrote detailed blogs throught the process - https://medium.com/@adipusk/list/end-to-end-mlops-project-c51ceb050829
## Demo

Insert gif or link to demo


## Run Locally

To deploy this project locally:

#### Steps 1: 
Clone the repo

```bash
  https://github.com/Puskchan/Cricket_Score_Predictor
```

#### Step 2:
Create a virtual environment

```bash
#Conda
conda create -n summary python=3.8 -y
conda activate summary
```

or

```bash
#venv
python3 -m venv venv
source /venv/bin/activate
```

#### Step 3:
Install requirements and run the app

```bash
pip install -r requirements.txt
```

```
# Finally run the following command
python app.py
```

Now the app will be up and running on your local host at port 5000.

## Deployment

For the Deployment part I would suggest that you go through my blogs and replicate the process. I have written every step that you can follow along. 

(Follow Part 8 - 1 & 2 from my blogs - linked above)


## Environment Variables

To deploy this project with AWS, you will need to add the following environment variables to your github secrets.

`AWS_ACCESS_KEY_ID`

`AWS_SECRET_ACCESS_KEY`

`AWS_REGION` 

`AWS_ECR_LOGIN_URI` 

`ECR_REPOSITORY_NAME` 

(All the material related to where and how can be found in my blogs - linked above)


## Appendix

Any additional information goes here


## Acknowledgements

 - [End to End data science playlist](https://www.youtube.com/playlist?list=PLZoTAELRMXVPS-dOaVbAux22vzqdgoGhG)

