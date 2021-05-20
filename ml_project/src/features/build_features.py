import numpy as np
import pandas as pd
import pickle
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler, MinMaxScaler

from entities import FeatureParams


def make_features(transformer: ColumnTransformer, df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(transformer.transform(df))


def build_transformer(params: FeatureParams) -> ColumnTransformer:
    transformer = ColumnTransformer(
        [
            (
                "categorical_pipeline",
                __build_categorical_pipeline(),
                params.categorical_features,
            ),
            (
                "numerical_pipeline",
                __build_numerical_pipeline(params),
                params.numerical_features,
            ),
        ]
    )
    return transformer


def serialize_transformer(transformer: ColumnTransformer, output: str):
    with open(output, "wb") as f:
        pickle.dump(transformer, f)


def deserialize_transformer(input_: str) -> ColumnTransformer:
    with open(input_, "rb") as f:
        transformer = pickle.load(f)
    return transformer


def process_categorical_features(categorical_df: pd.DataFrame) -> pd.DataFrame:
    categorical_pipeline = __build_categorical_pipeline()
    return pd.DataFrame(categorical_pipeline.fit_transform(categorical_df).toarray())


def process_numerical_features(numerical_df: pd.DataFrame) -> pd.DataFrame:
    num_pipeline = __build_numerical_pipeline()
    return pd.DataFrame(num_pipeline.fit_transform(numerical_df))


def extract_target(df: pd.DataFrame, params: FeatureParams) -> pd.Series:
    return df[params.target_col]


def __build_categorical_pipeline() -> Pipeline:
    categorical_pipeline = Pipeline(
        [
            ("impute", SimpleImputer(missing_values=np.nan, strategy="most_frequent")),
            ("ohe", OneHotEncoder()),
        ]
    )
    return categorical_pipeline


def __build_numerical_pipeline(feature_params: FeatureParams) -> Pipeline:
    num_pipeline = Pipeline(
        [("impute", SimpleImputer(missing_values=np.nan, strategy="mean"))]
    )

    if feature_params.preprocessing.numeric_scaler == "StandardScaler":
        num_pipeline.steps.append(("scaler", StandardScaler()))
    elif feature_params.preprocessing.numeric_scaler == "MinMaxScaler":
        num_pipeline.steps.append(("scaler", MinMaxScaler()))

    return num_pipeline
