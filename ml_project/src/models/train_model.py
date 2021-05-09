import pickle
import logging
import logging.config
import yaml

from typing import Union

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

from entities import TrainingParams

SklearnRegressionModel = Union[RandomForestClassifier, LogisticRegression]

logger = logging.getLogger(__name__)


def setup_logging(training_pipeline_params: TrainingParams):
    with open(training_pipeline_params.logging_config_path) as config_fin:
        config = yaml.safe_load(config_fin)
        logging.config.dictConfig(config)


def train_model(
        features: pd.DataFrame, target: pd.Series, train_params: TrainingParams
) -> SklearnRegressionModel:

    logger.info(f"training model with params {train_params}")
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


def serialize_model(model: SklearnRegressionModel, output: str) -> str:
    logger.info("serialize model")
    with open(output, "wb") as f:
        pickle.dump(model, f)
    return output
