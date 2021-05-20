import json
import logging
import sys
import yaml

import click

from data import read_data, split_train_val_data
from entities.train_pipeline_params import (
    TrainingPipelineParams,
    read_training_pipeline_params,
)
from features import make_features
from features.build_features import extract_target, build_transformer, serialize_transformer
from models import (
    train_model,
    serialize_model,
    predict_model,
    evaluate_model,
)

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)
logger.addHandler(handler)

def setup_logging(train_pipeline_params: TrainingPipelineParams):
    with open(train_pipeline_params.logging_config_path) as config_fin:
        config = yaml.safe_load(config_fin)
        logging.config.dictConfig(config)


def train_pipeline(training_pipeline_params: TrainingPipelineParams):
    logger.info(f"start train pipeline with params {training_pipeline_params}")
    data = read_data(training_pipeline_params.input_data_path)
    logger.info(f"data.shape is {data.shape}")
    train_df, val_df = split_train_val_data(
        data, training_pipeline_params.splitting
    )
    logger.info(f"train_df.shape is {train_df.shape}")
    logger.info(f"val_df.shape is {val_df .shape}")

    transformer = build_transformer(training_pipeline_params.features)
    transformer.fit(train_df.drop(columns=[training_pipeline_params.features.target_col]))
    serialize_transformer(transformer, training_pipeline_params.transformer_path)

    train_features = make_features(transformer, train_df.drop(columns=[training_pipeline_params.features.target_col]))
    train_target = extract_target(train_df, training_pipeline_params.features)

    logger.info(f"train_features.shape is {train_features.shape}")

    model = train_model(
        train_features, train_target, training_pipeline_params.train
    )

    val_features = make_features(transformer, val_df.drop(columns=[training_pipeline_params.features.target_col]))
    val_target = extract_target(val_df, training_pipeline_params.features)

    logger.info(f"val_features.shape is {val_features.shape}")
    predicts = predict_model(
        model,
        val_features
    )

    metrics = evaluate_model(
        predicts,
        val_target
    )

    with open(training_pipeline_params.metric_path, "w") as metric_file:
        json.dump(metrics, metric_file)
    logger.info(f"metrics is {metrics}")

    path_to_model = serialize_model(model, training_pipeline_params.output_model_path)

    return path_to_model, metrics


@click.command(name="training_pipeline")
@click.argument("config_path")
def train_pipeline_command(config_path: str):
    params = read_training_pipeline_params(config_path)
    train_pipeline(params)


if __name__ == "__main__":
    train_pipeline_command()
