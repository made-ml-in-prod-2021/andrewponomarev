from dataclasses import dataclass, field
from typing import List, Optional

from entities import PreprocessingParams


@dataclass()
class FeatureParams:
    categorical_features: List[str]
    numerical_features: List[str]
    features_to_drop: Optional[List[str]]
    preprocessing: Optional[PreprocessingParams]
    target_col: str = field(default="Good", compare=False)