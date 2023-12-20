import json
import pickle
from datetime import datetime

import pandas as pd

# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)


def preprocess_data(data):
    # Convert timestamp to datetime and extract features
    timestamp = datetime.strptime(data["timestamp"], "%d/%m/%Y %H:%M")
    hour = timestamp.hour
    day_of_week = timestamp.weekday()
    month = timestamp.month

    # Create a DataFrame from the request data
    df = pd.DataFrame(
        [
            [
                data['t1'],
                data['t2'],
                data['hum'],
                data['wind_speed'],
                data['weather_code'],
                data['is_holiday'],
                data['is_weekend'],
                data['season'],
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


def lambda_handler(event, context):
    # Directly use event as the input data
    data = event

    # Preprocess the input data
    processed_data = preprocess_data(data)

    # Make prediction
    prediction = model.predict(processed_data)

    # Convert numpy.float32 to Python float
    prediction_value = float(prediction[0])

    # Return the prediction
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"prediction": prediction_value}),
    }
