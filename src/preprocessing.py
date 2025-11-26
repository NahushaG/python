import pandas as pd
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

def load_data(csv_path):
    df = pd.read_csv(csv_path)
    return df

def preprocess_feature(df, fit_scaler=True):
    features = ["age","height_cm","weight_kg","goals_last_season","assists_last_season",
                "matches_played","injury_days_last_year","sprint_speed_mps","stamina_score"]
    
    X = df[features]

    if fit_scaler:
        X_scaled = scaler.fit_transform(X)
    else:
        X_scaled = scaler.transform(X)
    return X_scaled


