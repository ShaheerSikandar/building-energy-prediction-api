# Building Energy Prediction API

This project predicts building heating load using a Linear Regression model trained on the Energy Efficiency dataset.

## Features
- Data cleaning using Pandas
- Linear Regression model using scikit-learn
- Model evaluation using MAE, RMSE, and R2 score
- FastAPI prediction endpoint
- Minimal HTML frontend
- Dockerized application

## Tech Stack
- Python
- Pandas
- NumPy
- scikit-learn
- FastAPI
- Docker

## API Endpoint

POST /predict

Example input:

```json
{
  "relative_compactness": 0.98,
  "surface_area": 514.5,
  "wall_area": 294.0,
  "roof_area": 110.25,
  "overall_height": 7.0,
  "orientation": 2,
  "glazing_area": 0.0,
  "glazing_area_distribution": 0
} 
```

## Run Locally

Start API:

```bash
uvicorn app.main:app --reload
```
Open Swagger Docs:
http://127.0.0.1:8000/docs

## Frontend

- Open:frontend/index.html in your browser.

## Run with Docker

Build image:

```bash
docker build -t energy-prediction-api .
```

Run container:

```bash
docker run -p 8000:8000 energy-prediction-api
```

Open:

http://127.0.0.1:8000/docs