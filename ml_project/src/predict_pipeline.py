import logging
import yaml
import sys

import click

from data import read_data
from entities.predict_pipeline_params import (
    PredictPipelineParams,
    read_predict_pipeline_params,
)
from features import make_features
from features.build_features import deserialize_transformer
from models import (
    deserialize_model,
    serialize_prediction,
    predict_model
)

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def setup_logging(predict_pipeline_params: PredictPipelineParams):
    with open(predict_pipeline_params.logging_config_path) as config_fin:
        config = yaml.safe_load(config_fin)
        logging.config.dictConfig(config)


def predict_pipeline(predict_pipeline_params: PredictPipelineParams) -> str:
    logger.info(f"start predict pipeline with params {predict_pipeline_params}")
    data = read_data(predict_pipeline_params.input_data_path)
    logger.info(f"data.shape is {data.shape}")

    model = deserialize_model(predict_pipeline_params.model_path)

    transformer = deserialize_transformer(predict_pipeline_params.transformer_path)
    transformed_data = make_features(transformer, data)

    predicts = predict_model(
        model,
        transformed_data
    )

    path_to_prediction = serialize_prediction(predict_pipeline_params.predict_result_path, predicts)
    logger.info(f"prediction ready in path {path_to_prediction}")
    return path_to_prediction


@click.command(name="predict_pipeline")
@click.argument("config_path")
def predict_pipeline_command(config_path: str):
    params = read_predict_pipeline_params(config_path)
    predict_pipeline(params)


if __name__ == "__main__":
    predict_pipeline_command()
