import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# File names for cricket data (replace with your actual file names)
data_files = {
    "T20": "T20_matches.csv",
    "ODI": "ODI_matches.csv",
    "IPL": "IPL_matches.csv"
}

# Output file name for preprocessed data (replace as needed)
preprocessed_data_file = "preprocessed_data.pkl"

def preprocess_data():
  """
  This function reads cricket match data, preprocesses it, and saves it for model training.
  """
  data = pd.DataFrame()
  for name, filename in data_files.items():
    # Read data from each CSV file
    data_part = pd.read_csv(filename)
    data = pd.concat([data, data_part], ignore_index=True)

  # Handle missing values (replace with a strategy of your choice)
  data.fillna(data.mean(), inplace=True)

  # Identify categorical features
  categorical_features = ["bat_team", "bowl_team"]
  encoder = OneHotEncoder(sparse=False)
  encoded_data = pd.concat([data, pd.DataFrame(encoder.fit_transform(data[categorical_features]))], axis=1)
  encoded_data.drop(categorical_features, axis=1, inplace=True)

  # Identify numerical features
  numerical_features = ["runs", "wickets", "overs", "runs_last_5", "wickets_last_5"]
  scaler = StandardScaler()
  encoded_data[numerical_features] = scaler.fit_transform(encoded_data[numerical_features])

  # Save the preprocessed data for model training
  encoded_data.to_pickle(preprocessed_data_file)

if __name__ == "__main__":
  preprocess_data()
  print(f"Preprocessed data saved to: {preprocessed_data_file}")