import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
from preprocessing import preprocess_feature

def train_models(df):
    X = preprocess_feature(df, fit_scaler= True)
    Y_success = df["success_score"]
    Y_risk = df["risk_score"]

    success_model = RandomForestRegressor(n_estimators=100, random_state=42)
    success_model.fit(X,Y_success)
    
    risk_model = RandomForestRegressor(n_estimators=100, random_state=42)
    risk_model.fit(X,Y_risk)

    #Save models
    joblib.dump(success_model, "../models/success_model.pkl")
    joblib.dump(risk_model, "../models/risk_model.pkl")

    print("Model trained and saved successfully.")

def load_models():
    success_model = joblib.load("../models/success_model.pkl")
    risk_model = joblib.load("../models/risk_model.pkl")
    return success_model, risk_model

def predict(player_df, success_model, risk_model):
    X = preprocess_feature(player_df, fit_scaler=False)
    success_pred = success_model.predict(X)
    risk_pred = risk_model.predict(X)
    return success_pred[0], risk_pred[0]

    
