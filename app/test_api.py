"""
Some functions to test if our API is working properly.
"""

#  MANAGEMENT ENVIRONMENT --------------------------------
from fastapi.testclient import TestClient
from api import app

client = TestClient(app)


#  BUILD TEST FUNCTIONS --------------------------------
def test_read_welcome():
    """
    Verifies that the server correctly returns the welcome message.
    Sends a GET request to the endpoint and expects
    a 200 OK Request response from the server.
    """
    response = client.get("/Welcome")
    assert (response.status_code == 200)


def test_update_prediction():
    """
    Verifies that the server correctly returns the prediction.
    Sends a PUT request to the endpoint and expects
    a prediction (str) from the server.
    """
    url = "/Prediction"
    data = {"education": "primary", "duration": 3456, "age": 62,
            "contact": "cellular", "month": "jan", "default": "yes",
            "poutcome": "success", "pdays": 8, "day": 6, "loan": "yes",
            "campaign": 6, "marital": "divorced", "previous": -1,
            "balance": 6789, "job": "management", "housing": "yes"
            }
    response = client.put(url, data=data)
    assert (response.json() in
            [{'result': 'Prediction for the given features: deposit ✔️'},
            {'result': "Prediction for the given features: no deposit ❌"}]
            )


def test_update_prediction_format():
    """
    Tests whether the API correctly handles negative values
    for the 'age' parameter in the PUT request to the '/Prediction' endpoint.
    Sends a PUT request to the endpoint with a negative 'age' value and expects
    a 400 Bad Request response from the server.
    """
    url = "/Prediction"
    data = {"education": "primary", "duration": 3456, "age": -62,
            "contact": "cellular", "month": "jan", "default": "yes",
            "poutcome": "success", "pdays": 8, "day": 6, "loan": "yes",
            "campaign": 6, "marital": "divorced", "previous": -1,
            "balance": 6789, "job": "management", "housing": "yes"
            }
    response = client.put(url, data=data)
    assert (response.status_code == 400)


def test_update_prediction_missing_value():
    """
    Tests whether the API correctly handles missing values
    for the 'age' parameter in the PUT request to the '/Prediction' endpoint.
    Sends a PUT request to the endpoint with a missing 'age' value and expects
    a 400 Bad Request response from the server.
    """
    url = "/Prediction"
    data = {"education": "primary", "duration": 3456,
            "contact": "cellular", "month": "jan", "default": "yes",
            "poutcome": "success", "pdays": 8, "day": 6, "loan": "yes",
            "campaign": 6, "marital": "divorced", "previous": -1,
            "balance": 6789, "job": "management", "housing": "yes"
            }
    response = client.put(url, data=data)
    assert (response.status_code == 400)
