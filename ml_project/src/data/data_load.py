import pandas as pd
import logging
import logging.config
import yaml
from sklearn.model_selection import train_test_split
from typing import Tuple

from entities import SplittingParams, TrainingParams

logger = logging.getLogger(__name__)


def setup_logging(training_pipeline_params: TrainingParams):
    with open(training_pipeline_params.logging_config_path) as config_fin:
        config = yaml.safe_load(config_fin)
        logging.config.dictConfig(config)


def read_data(path: str) -> pd.DataFrame:
    logging.info(f"reading data from {path}")
    data = pd.read_csv(path)
    return data


def save_data(data: pd.DataFrame, path: str) -> pd.DataFrame:
    logging.info(f"saving data to csv to {path}")
    data.to_csv(path)
    return data


def split_train_val_data(
    data: pd.DataFrame, params: SplittingParams
) -> Tuple[pd.DataFrame, pd.DataFrame]:

    logging.info(f"splitting data to train and validation")
    train_data, val_data = train_test_split(
        data, test_size=params.val_size, random_state=params.random_state
    )
    return train_data, val_data