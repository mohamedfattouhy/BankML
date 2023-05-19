#!/bin/bash

# Run the main file (with 1 tree) and the API.
python3 main.py 1
python3 api.py
# uvicorn api:app --reload --host "0.0.0.0" --port 8000
