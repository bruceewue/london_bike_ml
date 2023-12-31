# London Bike Sharing Prediction

## Problem Description
This project aims to predict the bike sharing demand in London. The prediction is based on weather conditions and the date & time. The data used for this project is from the `london_merged.csv` file which contains historical data of weather conditions, date, time, and the number of bikes shared.
## Dataset

The dataset used in this project is `london_merged.csv`. This dataset contains the hourly data from three years (2015 - 2017) of the bike sharing program in London. The data was collected from different weather stations around the city.

Here are the columns in the dataset:

- `timestamp`: The date and hour of the data in format `dd/mm/yyyy hh:mm`.
- `cnt`: The count of new bike shares.
- `t1`: Real temperature in Celsius.
- `t2`: Temperature in Celsius "feels like".
- `hum`: Humidity in percentage.
- `wind_speed`: Wind speed in km/h.
- `weather_code`: Category of the weather (1: clear ; 2: scattered clouds / few clouds ; 3: broken clouds ; 4: cloudy ; 7: rain/ light Rain shower ; 10: rain with thunderstorm ; 26: snowfall ; 94: Freezing Fog).
- `is_holiday`: Boolean field - 1 holiday / 0 non holiday.
- `is_weekend`: Boolean field - 1 if the day is weekend.
- `season`: Season (0:spring ; 1:summer ; 2:fall ; 3:winter).

Please note that the `cnt` column is the target variable you will predict.

## Installation and Setup

This project uses Poetry for dependency management. To install the dependencies and activate the environment, follow these steps:

1. Install Poetry if you haven't already
2. Navigate to the project directory and install the dependencies:

```sh
cd london_bike_ml
poetry install
```

3. Activate the Poetry environment:

```sh
poetry shell
```

## Data Analysis and Model Training

For exploratory data analysis, refer to the [`analysis.ipynb`](command:_github.copilot.openRelativePath?%5B%22analysis.ipynb%22%5D "analysis.ipynb") notebook. 

To train the model, run the [`train.py`](command:_github.copilot.openRelativePath?%5B%22train.py%22%5D "train.py") script. This will generate a [`model.pkl`](command:_github.copilot.openRelativePath?%5B%22model.pkl%22%5D "model.pkl") file:

```sh
python train.py
```

## Local Deployment

You can test the local deployment by running the [`predict.py`](command:_github.copilot.openRelativePath?%5B%22predict.py%22%5D "predict.py") script:

```sh
python predict.py
```

The application will be accessible at `http://localhost:8000`.

## Dockerization

To build a Docker image of the application, use the following command:

```sh
docker build -t london_bike_ml .
```

To run the Docker container:

```sh
docker run -p 8000:8000 london_bike_ml
```

## AWS Deployment

The [`lambda_function.py`](command:_github.copilot.openRelativePath?%5B%22lambda_function.py%22%5D "lambda_function.py") script is used for deploying the model to AWS Lambda. 

To push the Docker image to Amazon ECR and create a new Lambda function, follow the instructions in the AWS documentation.

## Testing the API

Once the application is deployed, you can test it by sending a POST request to the API endpoint:

```sh
curl -X POST -H "Content-Type: application/json" -d '{
    "timestamp": "02/07/2021 14:00",
    "t1": 15.0,
    "t2": 13.0,
    "hum": 50.0,
    "wind_speed": 15.0,
    "weather_code": 1.0,
    "is_holiday": 0,
    "is_weekend": 0,
    "season": 1
}' https://utnnwrhlhe.execute-api.eu-west-2.amazonaws.com/beta/
```

## Final Result

Here is the final result of the AWS Lambda deployment:

![AWS Lambda Deployment](lambda.png)