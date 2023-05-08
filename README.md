# Prediction project on the data bank dataset

[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) 

This Git repository contains a (personal) prediction project on the bank dataset. The main goal is not the prediction itself, but rather to be able to build a modular, portable and reproducible project structure.

The project is organized in several directories:
- **src/bankml**: contains the scripts for training and evaluating the models.
- **model**: contains a *random forest* trained on the data for prediction.
- **configuration**: contains a yaml file to store some variables.
- **app**: contains an api to use our ML model (random forest).

The project is based on the following Git repository: https://github.com/ensae-reproductibilite/application-correction. This project has been designed to illustrate the different steps that separate the development phase of a project from the production phase.

## Instructions

To execute this project, you can follow these steps:

1. Clone the Git repository on your computer `git clone <project link>`.
2. Run the `install.sh` file in a terminal.
3. To train the ML model (random forest), run in a terminal `python main.py` or `python main.py <N_TREES>` to perform data collection, data preparation, training and model evaluation. In case you choose to specify **N_TREES**, make sure it is an integer greater than or equal to 1, as it indicates the number of trees in the random forest.

## API

An API is available to expose our machine learning model. I used FastAPI, which is a web framework for building RESTful APIs in Python.
The official documentation of FastAPI is available here: https://fastapi.tiangolo.com/

To execute the API, you can follow these steps:

1. Access the API file : `cd app/`
2. To run the API locally from a terminal, use the following command line : `python api.py`
