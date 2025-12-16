from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI(
    title="Credit Card Fraud Detection API",
    description="API for predicting credit card fraud using ML model.",
    version="1.0.0"
)

try:
    model = pickle.load(open("credit_fraud.pkl", "rb"))
except Exception as e:
    raise RuntimeError(f"Failed to load model: {e}")

class InputData(BaseModel):
    feature1: float
    feature2: float
    feature3: float

@app.post("/predict", tags=["Prediction"])
async def predict(data: InputData):
    try:
        features = np.array([[data.feature1, data.feature2, data.feature3]])
        prediction = model.predict(features)
        return {"prediction": int(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")
