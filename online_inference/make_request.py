import json
import requests

import pandas as pd

DATA_PATH = "data/heart.csv"


if __name__ == "__main__":
    data = pd.read_csv(DATA_PATH)
    data["id"] = range(len(data))
    request_data = data.to_dict(orient="records")
    print("Request data:")
    print(request_data)
    response = requests.post(
        "http://0.0.0.0:8000/predict",
        json.dumps(request_data)
    )
    print(f"Response status code: {response.status_code}")
    print("Response data:")
    print(response.json())
