from flask import Flask, request, jsonify

app = Flask(__name__)
import cricket_model  
@app.route("/predict", methods=["POST"])
def predict():
  try:
    data = request.get_json()
    match_type = data["matchType"]
    batting_team = data["battingTeam"]
    bowling_team = data["bowlingTeam"]
    current_score = data["currentScore"]
    current_overs = data["currentOvers"]
    wickets_fallen = data["wicketsFallen"]
    preprocessed_data = [match_type, batting_team, bowling_team, current_score, current_overs, wickets_fallen]
    prediction = cricket_model.predict_score(preprocessed_data)

    return jsonify({"score": prediction})
  except Exception as e:
    return jsonify({"error": str(e)}), 400 

if __name__ == "__main__":
  app.run(debug=True)