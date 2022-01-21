FROM python:3.7-slim

RUN mkdir src

WORKDIR /src

COPY model.joblib .
COPY requirements.txt .
COPY main.py .

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--reload", "--host=0.0.0.0", "--port=8000"]

# build image:                          docker build -t af/lp-service .
# create container from image:          docker run -p 8000:8000 af/lp-service
