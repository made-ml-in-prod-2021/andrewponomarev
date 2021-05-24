import pandas as pd
import numpy as np
import json

import pytest
from fastapi.testclient import TestClient

from app import app, load_model, load_transformer
from src.entities import HeartDiseaseData, PredictionResponse


client = TestClient(app)


@pytest.fixture(scope="session", autouse=True)
def initialize_model():
    load_model()
    load_transformer()


@pytest.fixture()
def test_data():
    data = [HeartDiseaseData(id=0), HeartDiseaseData(id=1)]
    return data


def test_predict_should_response_200(test_data):

    response = client.post("/predict",
                           data=json.dumps([x.__dict__ for x in test_data])
                           )
    assert 200 == response.status_code
    assert len(response.json()) == len(test_data)
    assert response.json()[0]["target"] in {0, 1}


def test_predict_should_response_422_with_wrong_type():
    with TestClient(app) as client:
        data = HeartDiseaseData()
        data.id = "asdsad"
        response = client.post("/predict", data=json.dumps([data.__dict__]))
        assert 422 == response.status_code

