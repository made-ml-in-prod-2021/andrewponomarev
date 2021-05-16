import os
import pickle
from typing import Tuple

from os.path import join

import pandas as pd
import pytest
from py._path.local import LocalPath
from sklearn.ensemble import RandomForestRegressor
from src.entities import FeatureParams, PreprocessingParams, TrainingParams
from tests import FAKE_DATASET_SIZE, FAKE_DATASET_NAME, CATEGORICAL_FEATURES, NUMERICAL_FEATURES, TARGET_FEATURES 
from sklearn.preprocessing import MinMaxScaler
from src.data import read_data
from src.features import build_transformer, make_features, extract_target
from src.models import train_model, serialize_model
from tests.test_utils import make_data
from sklearn.ensemble import RandomForestClassifier

@pytest.fixture()
def dataset_path(tmpdir) -> str:
    data = make_data(FAKE_DATASET_SIZE)
    path = join(tmpdir, FAKE_DATASET_NAME)
    data.to_csv(path, index=False)
    return path


@pytest.fixture
def features_and_target(
    dataset_path: str
) -> Tuple[pd.DataFrame, pd.Series]:
    params = FeatureParams(
        categorical_features=CATEGORICAL_FEATURES,
        numerical_features=NUMERICAL_FEATURES,
        features_to_drop=[],
        target_col=TARGET_FEATURES,
        preprocessing=PreprocessingParams(numeric_scaler=MinMaxScaler())
    )
    data = read_data(dataset_path)
    transformer = build_transformer(params)
    transformer.fit(data)
    features = make_features(transformer, data)
    target = extract_target(data, params)
    return features, target


@pytest.fixture()
def train_params() -> TrainingParams:
    params = TrainingParams(
        model_type="RandomForestClassifier",
        random_state=255,
        criterion="gini",
        n_estimators=100,
        max_depth=4
    )
    return params


def test_train_model(features_and_target: Tuple[pd.DataFrame, pd.Series], train_params: TrainingParams):
    features, target = features_and_target
    model = train_model(features, target, train_params)
    assert isinstance(model, RandomForestClassifier)
    assert model.predict(features).shape[0] == target.shape[0]


def test_serialize_model(tmpdir: LocalPath):
    expected_output = tmpdir.join("model.pkl")
    n_estimators = 10
    model = RandomForestRegressor(n_estimators=n_estimators)
    real_output = serialize_model(model, expected_output)
    assert real_output == expected_output
    assert os.path.exists
    with open(real_output, "rb") as f:
        model = pickle.load(f)
    assert isinstance(model, RandomForestRegressor)