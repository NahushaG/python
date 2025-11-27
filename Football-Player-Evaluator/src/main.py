import pandas as pd
from model import train_models, load_models, predict
from preprocessing import load_data

# Load sample data
data_path = "../data/sample_players.csv"
df = load_data(data_path)

# Train models (only once)
train_models(df)

# Load models
success_model, risk_model = load_models()

# Example: Predict a new player
new_player = pd.DataFrame([{
    "age": 22, "height_cm": 178, "weight_kg": 72, "position": "Forward",
    "goals_last_season": 10, "assists_last_season": 4, "matches_played": 25,
    "injury_days_last_year": 3, "sprint_speed_mps": 8.0, "stamina_score": 80
}])

success_score, risk_score = predict(new_player, success_model, risk_model)

print(f"Predicted Success Score: {success_score:.1f}/100")
print(f"Predicted Risk Score: {risk_score:.1f}/100")

# Optional textual explanation
print("\nRecommendation:")
if success_score > 75:
    print("- High potential. Consider for first team and advanced training.")
elif success_score > 60:
    print("- Moderate potential. Monitor performance and provide support.")
else:
    print("- Low potential. Focus on skill development and monitoring.")

if risk_score > 40:
    print("- High risk: Monitor fitness and injury prevention closely.")
elif risk_score > 20:
    print("- Moderate risk: Regular fitness monitoring advised.")
else:
    print("- Low risk: Standard monitoring sufficient.")
