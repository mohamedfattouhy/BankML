"""A simple API to expose our model
(RandomForest) trained to predict a deposit
in the bank after a marketing campaign."""

#  MANAGEMENT ENVIRONMENT --------------------------------
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from features.features_class import (
    Job,
    Marital,
    EducationLevel,
    Default,
    Housing,
    Loan,
    Contact,
    Month,
    Poutcoume,
)
from joblib import load
import pandas as pd
import subprocess
import os

model = load("../model/random_forest_bank.joblib")

app = FastAPI(
    title="Prediction of deposit in a bank",
    description="<center>Application to predict deposits at a bank\
                after a marketing campaign.\
                <br>An API version to facilitate the reuse of the model 🚀"
                + '<br><br><img \
                src="https://cdn.pixabay.com/photo/2015/08/29/20/21/safe-913452_1280.jpg"\
                width="250"> </center>'
)


# BUILD PAGES --------------------------------


@app.get("/Welcome", tags=["Welcome"], response_class=HTMLResponse)
def welcome_page() -> str:
    """
    Welcome page with model name, version, and
    link to 'Prediction' and 'docs' sections.

    Returns:
    str: The welcome message in html format.
    """

    welcome_message = "Welcome 🏴\
           <br> This is an API for predicting a deposit in a bank 🌐\
           <br> Model name: BankML\
           <br> Model version: 0.3\
           <br> To change features: Press 'Try it out' in\
           'Prediction' section ➔\
           <a href='http://127.0.0.1:8000/docs' target='_blank'\
           style='text-decoration:none; background: #fff;\
           border: 1px dashed;'>Docs</a>"

    return welcome_message


@app.put("/Prediction", tags=["Prediction"])
async def predict(
    education: EducationLevel,
    marital: Marital,
    job: Job,
    default: Default,
    contact: Contact,
    loan: Loan,
    housing: Housing,
    month: Month,
    poutcome: Poutcoume,
    age: int = 62,
    duration: int = 38,
    campaign: int = 2,
    pdays: int = 8,
    previous: int = 10,
    balance: int = 289,
    day: int = 12,
) -> str:

    """
    Prediction page which uses the trained model and
    returns the prediction for the given features.

    Returns:
    str: the prediction for the given features.
    """

    df_new = pd.DataFrame(
        {
            "age": [age],
            "job": [job.name],
            "marital": [marital.name],
            "education": [education.name],
            "default": [default.name],
            "balance": [balance],
            "housing": [housing.name],
            "loan": [loan.name],
            "contact": [contact.name],
            "day": [day],
            "month": [month.name],
            "duration": [duration],
            "campaign": [campaign],
            "pdays": [pdays],
            "previous": [previous],
            "poutcome": [poutcome.name]
        }
    )

    prediction = (
        "Prediction for the given features: deposit ✔️"
        if model.predict(df_new) == "yes"
        else "Prediction for the given features: no deposit ❌"
    )

    return HTMLResponse(prediction, media_type="text/html")


def main():
    if os.name == "posix":  # Linux/Mac OS system
        subprocess.call(["open", "http://127.0.0.1:8000/Welcome"])
        subprocess.call(["uvicorn", "api:app", "--reload", "--port", "8000"])
    if os.name == "nt":  # Windows system
        os.system("start http://127.0.0.1:8000/Welcome")
        subprocess.call(["uvicorn", "api:app", "--reload", "--port", "8000"])


if __name__ == "__main__":
    main()
