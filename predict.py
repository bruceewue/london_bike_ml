# predict.py
import pickle
from datetime import datetime

import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

app = FastAPI()


class BikeData(BaseModel):
    timestamp: str
    t1: float
    t2: float
    hum: float
    wind_speed: float
    weather_code: float
    is_holiday: int
    is_weekend: int
    season: int


def preprocess_data(data: BikeData):
    """
    Preprocess the request data to match the training data format.
    :param data: Input data from the request
    :return: Processed data ready for prediction
    """
    # Convert timestamp to datetime and extract features
    timestamp = datetime.strptime(data.timestamp, "%d/%m/%Y %H:%M")
    hour = timestamp.hour
    day_of_week = timestamp.weekday()
    month = timestamp.month

    # Create a DataFrame from the request data
    df = pd.DataFrame(
        [
            [
                data.t1,
                data.t2,
                data.hum,
                data.wind_speed,
                data.weather_code,
                data.is_holiday,
                data.is_weekend,
                data.season,
                hour,
                day_of_week,
                month,
            ]
        ],
        columns=[
            't1',
            't2',
            'hum',
            'wind_speed',
            'weather_code',
            'is_holiday',
            'is_weekend',
            'season',
            'hour',
            'day_of_week',
            'month',
        ],
    )

    return df


@app.post("/predict")
def predict(data: BikeData):
    # Preprocess the request data
    processed_data = preprocess_data(data)

    # Make prediction
    prediction = model.predict(processed_data)

    # Return the prediction
    return {"prediction": prediction[0]}


# Optional: If you want to start the server using this script
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
