from dataclasses import dataclass, field


@dataclass()
class TrainingParams:
    model_type: str = field(default="RandomForestRegressor")
    random_state: int = field(default=255)
    criterion: str = field(default="gini")
    n_estimators: int = field(default=100)
    max_depth: int = field(default=4)
