"""A simple API to expose our model
RandomForest trained to predict a deposit
in the bank after a marketing campaign."""

#  MANAGEMENT ENVIRONMENT --------------------------------
from fastapi import FastAPI
from joblib import load
import pandas as pd

model = load("../model/random_forest_bank.joblib")

app = FastAPI(
    title="Prediction of deposit in a bank",
    description="<center>Application to predict deposits at a bank\
                 after a marketing campaign.\
                 <br>An API version to facilitate the reuse of the model 🚀"
    + '<br><br><img \
                 src="https://cdn.pixabay.com/photo/2015/08/29/20/21/safe-913452_1280.jpg"\
                width="250"> </center>',
)


# BUILD PAGES --------------------------------


@app.get("/Welcome", tags=["Welcome"])
def welcome_page() -> dict:
    """
    welcome page with model name and version.
    """

    welcome_message = {
        "Message": "Welcome, this is an API"
        "for predicting a deposit in a bank",
        "Model name": "BankML",
        "Model version": "0.1"
    }

    return welcome_message


@app.get("/Prediction", tags=["Prediction"])
def predict(
    age: int = 62,
    job: str = "services",
    marital: str = "married",
    education: str = "secondary",
    default: str = "no",
    balance: int = 289,
    housing: str = "127",
    loan: float = 125.0,
    contact: str = "telephone",
    day: int = "15",
    month: str = "may",
    duration: int = 38,
    campaign: int = 2,
    pdays: int = 8,
    previous: int = 10,
    poutcome: str = "sucess",
) -> str:
    """ """

    df_new = pd.DataFrame(
        {
            "age": [age],
            "job": [job],
            "marital": [marital],
            "education": [education],
            "default": [default],
            "balance": [balance],
            "housing": [housing],
            "loan": [loan],
            "contact": [contact],
            "day": [day],
            "month": [month],
            "duration": [duration],
            "campaign": [campaign],
            "pdays": [pdays],
            "previous": [previous],
            "poutcome": [poutcome],
        }
    )

    prediction = (
        "Prediction for the given"
        "features: Deposit ✔️"
        if model.predict(df_new) == "yes"
        else "Prediction for"
             "the given features: No-deposit ❌"
    )

    return prediction
