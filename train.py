# train.py
import pickle

import pandas as pd

# from xgboost import XGBRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split


# Load and preprocess the dataset
def load_and_preprocess_data(filepath):
    """
    Load and preprocess the dataset.
    :param filepath: Path to the CSV file
    :return: Processed DataFrame
    """
    # Load the dataset
    data = pd.read_csv(filepath)

    # Convert timestamp to datetime and extract features
    data['timestamp'] = pd.to_datetime(data['timestamp'], format="%d/%m/%Y %H:%M")
    data['hour'] = data['timestamp'].dt.hour
    data['day_of_week'] = data['timestamp'].dt.dayofweek
    data['month'] = data['timestamp'].dt.month

    # Drop the original timestamp column
    data = data.drop(['timestamp'], axis=1)

    return data


# Load the dataset
file_path = 'data/london_merged.csv'
data = load_and_preprocess_data(file_path)

# Splitting the data into features and target variable
X = data.drop('cnt', axis=1)
y = data['cnt']

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
# best_params = {
#     'n_estimators': 275,
#     'max_depth': 8,
#     'learning_rate': 0.07070693871571615,
#     'min_child_weight': 1,
#     'subsample': 0.5609764636237523,
#     'colsample_bytree': 0.9347629599226998,
#     'gamma': 4.47355915479421,
# }
# model = XGBRegressor(**best_params)

model = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42)
model.fit(X_train, y_train)


# Save the trained model to a file
def save_model(model, filename):
    """
    Save the trained model to a pickle file.
    :param model: Trained model to be saved
    :param filename: Path where the model should be saved
    """
    with open(filename, 'wb') as file:
        pickle.dump(model, file)


# Saving the model
model_filename = 'model.pkl'
save_model(model, model_filename)

print(f"Model trained and saved as {model_filename}")
