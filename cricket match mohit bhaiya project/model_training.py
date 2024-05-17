from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.model_selection import train_test_split
import pickle

# File names for preprocessed data and trained model (replace as needed)
preprocessed_data_file = "preprocessed_data.pkl"
model_file = "cricket_model.pkl"

def train_model():
  """
  This function loads preprocessed data, trains a model (replace with your choice),
  evaluates its performance, and saves the trained model.
  """

  # Load preprocessed data
  encoded_data = pd.read_pickle(preprocessed_data_file)

  # Split data into features (X) and target variable (y)
  X = encoded_data.drop("total", axis=1)  # Features (all columns except "total")
  y = encoded_data["total"]  # Target variable (score)

  # Split data into training and testing sets
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

  # Choose and train a model (replace with your preferred model)
  # Here's an example using Random Forest Regressor
  model = RandomForestRegressor(n_estimators=100, random_state=42)
  model.fit(X_train, y_train)

  # Evaluate model performance (e.g., using Mean Squared Error)
  from sklearn.metrics import mean_squared_error
  y_pred = model.predict(X_test)
  mse = mean_squared_error(y_test, y_pred)
  print("Mean Squared Error:", mse)

  # Save the trained model for future use
  pickle.dump(model, open(model_file, "wb"))

  print(f"Model trained and saved to: {model_file}")

if __name__ == "__main__":
  train_model()