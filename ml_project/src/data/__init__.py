import sys
from .data_load import read_data, split_train_val_data

sys.modules[__name__] = sys.modules['data']

__all__ = [
    "read_data",
    "split_train_val_data"
]