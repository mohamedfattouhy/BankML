"""A simple API to expose our model
(RandomForest) trained to predict a deposit
in the bank after a marketing campaign."""

#  MANAGEMENT ENVIRONMENT --------------------------------
from fastapi import FastAPI, Form
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.responses import HTMLResponse, PlainTextResponse
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


description = (
    "<center>Application to predict deposits at a bank\
                 after a marketing campaign.\
                 <br>An API version to facilitate the reuse of the model 🚀"
    + '<br><br><img \
                 src="https://cdn.pixabay.com/photo/2015/08/29/20/21/safe-913452_1280.jpg"\
                 width="250"> </center>'
)


model = load("../model/random_forest_bank.joblib")

app = FastAPI(
    include_in_schema=1,
    title="Prediction of deposit in a bank",
    description=description,
    redoc_url=None,
)


# CHANGE ERROR DISPLAY --------------------------------

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)


# BUILD PAGES --------------------------------

@app.get("/Welcome", tags=" ", response_class=HTMLResponse)
def welcome_page() -> str:
    """
    **Description:** welcome page.

    **Returns:**
    <br>_str_ : the welcome message in html format.
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


@app.put("/Prediction", tags=" ")
async def predict(
    education: EducationLevel = Form(description=" "),
    marital: Marital = Form(..., description=" "),
    job: Job = Form(..., description=" "),
    default: Default = Form(..., description=" "),
    contact: Contact = Form(..., description=" "),
    loan: Loan = Form(..., description=" "),
    housing: Housing = Form(..., description=" "),
    month: Month = Form(..., description=" "),
    poutcome: Poutcoume = Form(..., description=" "),
    # age: Annotated[int, Query(gt=1, example=62)],
    age: int = Form(..., gt=0, example=52),
    duration: int = Form(..., gt=0),
    campaign: int = Form(..., gt=0),
    pdays: int = Form(...),
    previous: int = Form(...),
    balance: int = Form(..., gt=0),
    day: int = Form(...),
) -> dict:

    """
    **Description:** prediction page which uses the trained model and
    returns the prediction for the given features.

    **Returns:**
    <br>_str_ : the prediction for the given features.
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
            "poutcome": [poutcome.name],
        }
    )

    prediction = (
        "Prediction for the given features: deposit ✔️"
        if model.predict(df_new) == "yes"
        else "Prediction for the given features: no deposit ❌"
    )

    result = {"result": prediction}

    return result


def main():
    if os.name == "posix":  # Linux/Mac OS system
        subprocess.call(["open", "http://127.0.0.1:8000/Welcome"])
        subprocess.call(["uvicorn", "api:app", "--reload", "--port", "8000"])
    if os.name == "nt":  # Windows system
        os.system("start http://127.0.0.1:8000/Welcome")
        subprocess.call(["uvicorn", "api:app", "--reload", "--port", "8000"])


if __name__ == "__main__":
    main()
