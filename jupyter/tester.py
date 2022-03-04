import random

import pandas as pd
import requests


df_test = pd.read_csv('test.csv')
n = len(df_test)

for ix, row in df_test.iterrows():
    vector = list(row)

    if random.random() > .75:
        response_prediction = requests.post('http://localhost:8000/prediction/?score=false',
                                            json=vector)

    else:
        response_prediction = requests.post('http://localhost:8000/prediction/?score=true',
                                            json=vector)
    
    if ix % 100 == 0:
        print(f'Request {ix}/{n}: prediction for {vector} is {response_prediction.json()}')


response_model_information = requests.get("http://localhost:8000/model_information")
print(f'Model information: {response_prediction}')
