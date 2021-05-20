import pickle


from typing import Union

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

from entities import TrainingParams

SklearnClassificationModel = Union[RandomForestClassifier, LogisticRegression]


def train_model(
        features: pd.DataFrame, target: pd.Series, train_params: TrainingParams
) -> SklearnClassificationModel:

    if train_params.model_type == "RandomForestClassifier":
        model = RandomForestClassifier(
            n_estimators=100,
            criterion=train_params.criterion,
            max_depth=train_params.max_depth,
            random_state=train_params.random_state
        )
    elif train_params.model_type == "LogisticRegression":
        model = LogisticRegression(
            random_state=train_params.random_state
        )
    else:
        raise NotImplementedError()
    model.fit(features, target)
    return model


def serialize_model(model: SklearnClassificationModel, output: str) -> str:
    with open(output, "wb") as f:
        pickle.dump(model, f)
    return output
