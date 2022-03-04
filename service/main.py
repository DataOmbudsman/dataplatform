import time
from typing import List, Optional

import numpy as np
from joblib import load
from fastapi import FastAPI
from prometheus_client import Counter, Histogram, make_asgi_app

app = FastAPI()
app_metrics = make_asgi_app()
app.mount("/metrics", app_metrics)

counter_model_information = Counter('model_information', 'How many times model information was asked')
counter_predictions = Counter('prediction', 'How many times predictions were asked')
histogram_predictions = Histogram('prediction_output', 'Histogram of -1/1 predictions')
histogram_scores = Histogram('prediction_score', 'Histogram of predictions scores')
histogram_latency = Histogram('latency', 'Histogram of prediction latency')

model = load('model.joblib')


@app.get("/model_information")
def read_model_information():
    counter_model_information.inc()
    return model.get_params()


@app.post("/prediction/")
def read_item(feature_vector: List[float], score: Optional[bool]=False):
    t0 = time.time()

    counter_predictions.inc()

    feature_vector_array = np.array(feature_vector).reshape(1, -1)
    prediction = model.predict(feature_vector_array)[0]
    histogram_predictions.observe(int(prediction))

    response = {
        "is_inlier": int(prediction)
    }

    if score:
        anomaly_score = model.score_samples(feature_vector_array)[0]
        histogram_scores.observe(anomaly_score)
        response.update({
            "anomaly_score": anomaly_score
        })

    t1 = time.time()
    latency = t1 - t0
    histogram_latency.observe(latency)

    return response
