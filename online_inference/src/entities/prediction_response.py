from pydantic import BaseModel


class PredictionResponse(BaseModel):
    id: int
    target: int
