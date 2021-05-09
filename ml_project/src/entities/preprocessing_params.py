from dataclasses import dataclass, field
from typing import List, Optional


@dataclass()
class PreprocessingParams:
    numeric_scaler: str

