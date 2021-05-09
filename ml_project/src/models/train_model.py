import pickle
from typing import Union

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression

from entities import TrainingParams

SklearnRegressionModel = Union[RandomForestRegressor, LinearRegression]


def train_model(
        features: pd.DataFrame, target: pd.Series, train_params: TrainingParams
) -> SklearnRegressionModel:
    if train_params.model_type == "RandomForestRegressor":
        model = RandomForestRegressor(
            n_estimators=100, random_state=train_params.random_state
        )
    elif train_params.model_type == "LinearRegression":
        model = LinearRegression()
    else:
        raise NotImplementedError()
    model.fit(features, target)
    return model


def serialize_model(model: SklearnRegressionModel, output: str) -> str:
    with open(output, "wb") as f:
        pickle.dump(model, f)
    return output
