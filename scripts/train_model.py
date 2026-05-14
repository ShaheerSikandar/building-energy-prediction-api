import os
import joblib
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


DATA_PATH = "data/energy_efficiency.csv"
MODEL_PATH = "app/model/energy_model.pkl"


def load_data():
    df = pd.read_excel(DATA_PATH)

    df.columns = [
        "relative_compactness",
        "surface_area",
        "wall_area",
        "roof_area",
        "overall_height",
        "orientation",
        "glazing_area",
        "glazing_area_distribution",
        "heating_load",
        "cooling_load"
    ]

    df = df.drop_duplicates()

    return df


def train_model():
    df = load_data()

    X = df[
        [
            "relative_compactness",
            "surface_area",
            "wall_area",
            "roof_area",
            "overall_height",
            "orientation",
            "glazing_area",
            "glazing_area_distribution"
        ]
    ]

    y = df["heating_load"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    r2 = r2_score(y_test, predictions)

    print("Model training complete")
    print(f"MAE: {mae:.2f}")
    print(f"RMSE: {rmse:.2f}")
    print(f"R2 Score: {r2:.2f}")

    os.makedirs("app/model", exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    print(f"Model saved to {MODEL_PATH}")


if __name__ == "__main__":
    train_model()