import logging
import os
import pickle
import pandas as pd
import uvicorn

from typing import List, Union, Optional
from pydantic import BaseModel, conlist
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from fastapi import FastAPI, HTTPException

from src.entities import HeartDiseaseData, PredictionResponse
from src.validator import check_data

logger = logging.getLogger(__name__)


DEFAULT_MODEL_PATH = "model/model_lr.pkl"
DEFAULT_TRANSFORMER_PATH = "model/transformer.pkl"

def load_object(path: str) -> Pipeline:
    with open(path, "rb") as f:
        return pickle.load(f)


def make_predict(data: List[HeartDiseaseData], pipeline: Pipeline, transformer: ColumnTransformer) \
        -> List[PredictionResponse]:
    data = pd.DataFrame(row.__dict__ for row in data)
    ids = [int(x) for x in data.id]
    transformed_data = transformer.transform(data.drop("id", axis=1))
    predicts = pipeline.predict(transformed_data)

    return [
        PredictionResponse(id=id_, target=int(predict_))
        for id_, predict_ in zip(ids, predicts)
    ]


app = FastAPI()


@app.get("/")
def main():
    return "It is entry point of our predictor"


@app.on_event("startup")
def load_model():
    model_path = os.getenv("PATH_TO_MODEL", default=DEFAULT_MODEL_PATH)
    if model_path is None:
        err = f"PATH_TO_MODEL {model_path} is None"
        logger.error(err)
        raise RuntimeError(err)
    global model
    model = load_object(model_path)


@app.on_event("startup")
def load_transformer():
    transformer_path = os.getenv("PATH_TO_TRANSFORMER", default=DEFAULT_TRANSFORMER_PATH)
    if transformer_path is None:
        err = f"PATH_TO_TRANSFORMER {transformer_path} is None"
        logger.error(err)
        raise RuntimeError(err)
    global transformer
    transformer = load_object(transformer_path)


@app.get("/health")
def health() -> bool:
    return not (model is None)


@app.post("/predict", response_model=List[PredictionResponse])
def predict(request: List[HeartDiseaseData]):
    for data in request:
        is_valid, error_message = check_data(data)
        if not is_valid:
            raise HTTPException(status_code=400, detail=error_message)
    return make_predict(request, model, transformer)


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=os.getenv("PORT", 8000))