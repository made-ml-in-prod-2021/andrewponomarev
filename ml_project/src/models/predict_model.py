import numpy as np
import pandas as pd
import logging
import yaml
from typing import Dict, Union
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression

from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

from entities import TrainingParams

SklearnRegressionModel = Union[RandomForestRegressor, LinearRegression]

logger = logging.getLogger(__name__)


def setup_logging(training_pipeline_params: TrainingParams):
    with open(training_pipeline_params.logging_config_path) as config_fin:
        config = yaml.safe_load(config_fin)
        logging.config.dictConfig(config)


def predict_model(
        model: SklearnRegressionModel, features: pd.DataFrame) -> np.ndarray:

    logging.info("evaluating model ")
    predicts = model.predict(features)
    return predicts


def evaluate_model(
        predicts: np.ndarray, target: pd.Series) -> Dict[str, float]:

    logging.info("evaluating model ")
    return {
        "r2_score": r2_score(target, predicts),
        "rmse": mean_squared_error(target, predicts, squared=False),
        "mae": mean_absolute_error(target, predicts),
    }
