from os.path import join
from os import remove

import pandas as pd
import pytest

from src.entities import FeatureParams, PreprocessingParams
from tests import FAKE_DATASET_SIZE, FAKE_DATASET_NAME, CATEGORICAL_FEATURES, NUMERICAL_FEATURES, TARGET_FEATURES
from src.data import read_data
from src.features import build_transformer, make_features
from tests.test_utils import make_data
from sklearn.preprocessing import MinMaxScaler


@pytest.fixture()
def dataset_path(tmpdir) -> str:
    data = make_data(FAKE_DATASET_SIZE)
    path = join(tmpdir, FAKE_DATASET_NAME)
    data.to_csv(path, index=False)
    return path


def test_make_features(dataset_path: str):
    data = read_data(dataset_path)
    feature_params = FeatureParams(
        categorical_features=CATEGORICAL_FEATURES,
        numerical_features=NUMERICAL_FEATURES,
        features_to_drop=[],
        target_col=TARGET_FEATURES,
        preprocessing=PreprocessingParams(numeric_scaler=MinMaxScaler())
    )
    transformer = build_transformer(feature_params)
    transformer.fit(data)
    features = make_features(transformer, data)
    assert not pd.isnull(features).any().any()
    assert all(x not in features.columns for x in feature_params.features_to_drop)
    remove(dataset_path)
