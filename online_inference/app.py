import logging
import os
import pickle
import pandas as pd
import uvicorn

from typing import List, Union, Optional
from pydantic import BaseModel, conlist
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from fastapi import FastAPI

logger = logging.getLogger(__name__)


class HeartDiseaseModel(BaseModel):
    data: List[conlist(Union[float, str, int, None], min_items=13, max_items=13)]
    features: List[str]


## todo: уточнить в другой ветке
class HeartDiseaseResponse(BaseModel):
    target: bool


def load_object(path: str) -> Pipeline:
    with open(path, "rb") as f:
        return pickle.load(f)


def make_predict(
    data: List, features: List[str], model: Pipeline, transformer: ColumnTransformer
) -> List[HeartDiseaseResponse]:
    data = pd.DataFrame(data, columns=features)
    transformed_data = transformer.transform(data)
    predicts = model.predict(transformed_data)

    return [
        HeartDiseaseResponse(target=bool(target)) for target in predicts
    ]


app = FastAPI()


@app.get("/")
def main():
    return "It is entry point of our predictor"


@app.on_event("startup")
def load_model():
    global model
    model = load_object("model/model_lr.pkl")


@app.on_event("startup")
def load_transformer():
    global transformer
    transformer = load_object("model/transformer.pkl")


@app.get("/health")
def health() -> bool:
    return not (model is None)


@app.post("/predict/", response_model=List[HeartDiseaseResponse])
def predict(request: HeartDiseaseModel):
    return make_predict(request.data, request.features, model, transformer)


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=os.getenv("PORT", 8000))