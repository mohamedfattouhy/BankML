"""A simple API to expose our model
(RandomForest) trained to predict a deposit
in the bank after a marketing campaign."""

#  MANAGEMENT ENVIRONMENT --------------------------------
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
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
                 width="250"> </center>',
)


# BUILD PAGES --------------------------------


@app.get("/Welcome", tags=["Welcome"], response_class=HTMLResponse)
def welcome_page() -> str:
    """
    Welcome page with model name, version, and
    link to 'Prediction' and 'docs' sections.

    Returns: str with the welcome message in html format.
    """

    welcome_message = "Welcome 🏴\
           <br> This is an API for predicting a deposit in a bank 🌐\
           <br> Model name: BankML\
           <br> Model version: 0.2\
           <br> Go to ➔ <a href='http://127.0.0.1:8000/Prediction'\
            target='_blank' style='text-decoration:none;background: #fff;\
            border: 1px dashed;'>Prediction</a>\
           <br> To change features ➔\
            <a href='http://127.0.0.1:8000/docs' target='_blank'\
            style='text-decoration:none; background: #fff;\
            border: 1px dashed;'>Docs</a> in 'Prediction' section"

    return welcome_message


@app.get("/Prediction", tags=["Prediction"], response_class=HTMLResponse)
async def predict(
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

    """
    Prediction page which uses the trained model and
    returns the prediction for the given features.

    Returns: str with the given features and prediction in html format.
    """

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
        "Prediction for the given" "features: Deposit ✔️"
        if model.predict(df_new) == "yes"
        else "Prediction for" "the given features: No-deposit ❌"
    )

    # Creation of the HTML table from the DataFrame
    table_html = df_new.to_html(index=False, justify='center', border=3)

    html = f"""
        <html>
            <head>
                <title>Prediction Page</title>
            </head>
            <body>
                <div id="table_block">
                    <h3>Table:</h3>
                    {table_html}
                </div>
                <div id="prediction_block">
                    <h3>Prediction:</h3>
                    <p>{prediction}</p>
                </div>
            </body>
        </html>
    """
    return html


def main():
    if os.name == "posix":  # Linux/Mac OS system
        subprocess.call(["open", "http://127.0.0.1:8000/Welcome"])
        subprocess.call(["uvicorn", "api:app", "--reload", "--port", "8000"])
    if os.name == "nt":  # Windows system
        os.system("start http://127.0.0.1:8000/Welcome")
        subprocess.call(["uvicorn", "api:app", "--reload", "--port", "8000"])


if __name__ == "__main__":
    main()
