from array import array
import re
from typing import List, Optional

import numpy as np
from joblib import load
from fastapi import FastAPI

app = FastAPI()

model = load('model.joblib')


@app.get("/model_information")
def read_model_information():
    return model.get_params()


@app.post("/prediction/")
def read_item(feature_vector: List[float], score: Optional[bool]=False):
    feature_vector_array = np.array(feature_vector).reshape(1, -1)
    prediction = model.predict(feature_vector_array)[0]

    response = {
        "is_inlier": int(prediction)
    }

    if score:
        anomaly_score = model.score_samples(feature_vector_array)[0]
        response.update({
            "anomaly_score": anomaly_score
        })

    return response
