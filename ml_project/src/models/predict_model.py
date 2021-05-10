import numpy as np
import pandas as pd
import pickle
from typing import Dict, Union
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

SklearnRegressionModel = Union[RandomForestClassifier, LogisticRegression]


def predict_model(
        model: SklearnRegressionModel, features: pd.DataFrame) -> np.ndarray:
    predicts = model.predict(features)
    return predicts


def evaluate_model(
        predicts: np.ndarray, target: pd.Series) -> Dict[str, float]:
    return {
        "r2_score": r2_score(target, predicts),
        "rmse": mean_squared_error(target, predicts, squared=False),
        "mae": mean_absolute_error(target, predicts),
    }


def deserialize_model(path: str) -> SklearnRegressionModel:
    with open(path, "rb") as f:
        loaded_model = pickle.load(f)
    return loaded_model


def serialize_prediction(path: str, prediction: np.ndarray) -> str:
    prediction.tofile(path, sep=',', format='%10.5f')
    return path

