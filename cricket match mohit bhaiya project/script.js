const predictionForm = document.getElementById("predictionForm"); 

predictionForm.addEventListener("submit", function(event) {
  event.preventDefault(); 

  const data = {
    matchType: document.getElementById("match-type").value,
    battingTeam: document.getElementById("batting-team").value,
    bowlingTeam: document.getElementById("bowling-team").value,
    currentScore: document.getElementById("current-score").value,
    currentOvers: document.getElementById("current-overs").value,
    wicketsFallen: document.getElementById("wickets-fallen").value,
  };

  fetch("/predict", { 
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  })
    .then((response) => response.json()) 
    .then((data) => {
      document.getElementById("prediction-result").textContent = "Predicted Score: " + data.prediction;
    })
    .catch((error) => {
      console.error("Error:", error);
    });
});