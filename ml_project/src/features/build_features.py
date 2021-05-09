import numpy as np
import pandas as pd
import logging
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler, MinMaxScaler

from entities import FeatureParams, PreprocessingParams


def make_features(transformer: ColumnTransformer, df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(transformer.transform(df).toarray())


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
                __build_numerical_pipeline(),
                params.numerical_features,
            ),
        ]
    )
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


def __build_numerical_pipeline(preprocessing_params: PreprocessingParams) -> Pipeline:
    num_pipeline = Pipeline(
        [("impute", SimpleImputer(missing_values=np.nan, strategy="mean"))]
    )

    if preprocessing_params.scaler == "StandardScaler":
        num_pipeline.append(("scaler", StandardScaler()))
    elif preprocessing_params.scaler == "MinMaxScaler":
        num_pipeline.append(("scaler", MinMaxScaler()))

    return num_pipeline
