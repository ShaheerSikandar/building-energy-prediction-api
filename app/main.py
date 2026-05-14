import joblib
import numpy as np
from fastapi import FastAPI
from app.schemas import BuildingFeatures
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Building Energy Prediction API",
    description="A Linear Regression API that predicts heating load from building design features.",
    version="1.0.0"
    
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("app/model/energy_model.pkl")


@app.get("/")
def home():
    return {
        "message": "Building Energy Prediction API is running",
        "docs": "/docs"
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/predict")
def predict_heating_load(features: BuildingFeatures):
    input_data = np.array([
        [
            features.relative_compactness,
            features.surface_area,
            features.wall_area,
            features.roof_area,
            features.overall_height,
            features.orientation,
            features.glazing_area,
            features.glazing_area_distribution
        ]
    ])

    prediction = model.predict(input_data)[0]

    return {
        "predicted_heating_load": round(float(prediction), 2),
        "input_features": features.dict()
    }