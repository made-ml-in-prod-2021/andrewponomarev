FROM python:3.7-slim-stretch
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY src /src
COPY app.py /app.py
COPY model/model_lr.pkl /model/model_lr.pkl
COPY model/transformer.pkl /model/transformer.pkl

WORKDIR .

ENV PATH_TO_MODEL="model/model_lr.pkl"
ENV PATH_TO_TRANSFORMER="model/transformer.pkl"

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]