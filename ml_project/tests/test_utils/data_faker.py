import numpy as np
import pandas as pd
from typing import List


class CategoricalFeature:

    def __init__(self, name: str, enum: List[int], probs: List[float], size: int):
        self.name = name
        self.enum = enum
        self.probs = probs
        self.size = size
        self.values = np.random.choice(enum, size=size, replace=True, p=probs)


class NumericalFeature:

    def __init__(self, name: str, mean: float, std: float, size: int):
        self.name = name
        self.mean = mean
        self.std = std
        self.size = size
        self.values = np.random.normal(loc=mean, scale=std, size=size)



def make_data(size: int, seed: int = 11) -> pd.DataFrame:
    np.random.seed(seed)
    data = pd.DataFrame()

    sex_f = CategoricalFeature("sex", [1, 0], [0.65, 0.35], size)
    cp_f = CategoricalFeature("cp", [0, 1, 2, 3], [0.45, 0.15, 0.25, 0.15], size)
    fbs_f = CategoricalFeature("fbs", [0, 1], [0.7, 0.3], size)
    exang_f = CategoricalFeature("exang", [0, 1], [0.6, 0.4], size)
    restecg_f = CategoricalFeature("restecg", [0, 1], [0.44, 0.56], size)

    age_f = NumericalFeature("age", 50, 10, size)
    trestbps_f = NumericalFeature("trestbps", 130, 17, size)
    chol_f = NumericalFeature("chol", 245, 18, size)
    thalach_f = NumericalFeature("thalach", 150, 52, size)
    oldpeak_f = NumericalFeature("oldpeak", 1.04, 1.16, size)

    target_f = CategoricalFeature("target", [0, 1], [0.45, 0.55], size)

    data[sex_f.name] = sex_f.values
    data[cp_f.name] = cp_f.values
    data[fbs_f.name] = fbs_f.values
    data[exang_f.name] = exang_f.values
    data[restecg_f.name] = restecg_f.values
    data[age_f.name] = age_f.values
    data[trestbps_f.name] = trestbps_f.values
    data[chol_f.name] = chol_f.values
    data[thalach_f.name] = thalach_f.values
    data[oldpeak_f.name] = oldpeak_f.values
    data[target_f.name] = target_f.values

    return data
