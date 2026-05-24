from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import pickle
import numpy as np
import pandas as pd
import uvicorn
import os

app = FastAPI(
    title="Heart Disease Prediction API",
    description="ML API for predicting heart disease risk using clinical attributes",
    version="1.0.0"
)

templates = Jinja2Templates(directory="templates")

model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'best_model.pkl')
preprocessor_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'preprocessor.pkl')

with open(model_path, 'rb') as f:
    model = pickle.load(f)
with open(preprocessor_path, 'rb') as f:
    preprocessor = pickle.load(f)

FEATURE_NAMES = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
                 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/predict")
async def predict_get(
    age: float = 52,
    sex: int = 1,
    cp: int = 0,
    trestbps: float = 130,
    chol: float = 240,
    fbs: int = 0,
    restecg: int = 1,
    thalach: float = 150,
    exang: int = 0,
    oldpeak: float = 1.0,
    slope: int = 1,
    ca: float = 0,
    thal: float = 1
):
    try:
        features = pd.DataFrame([[age, sex, cp, trestbps, chol, fbs, restecg,
                                   thalach, exang, oldpeak, slope, ca, thal]],
                                columns=FEATURE_NAMES)
        features_processed = preprocessor.transform(features)
        prediction = int(model.predict(features_processed)[0])
        probability = float(model.predict_proba(features_processed)[0, 1])

        result = {
            "prediction": prediction,
            "prediction_text": "Heart Disease Detected" if prediction == 1 else "No Heart Disease",
            "probability": round(probability, 4),
            "risk_level": "High" if probability > 0.7 else "Moderate" if probability > 0.3 else "Low"
        }
        return JSONResponse(content=result)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)

@app.post("/predict", response_class=HTMLResponse)
async def predict_post(
    request: Request,
    age: float = Form(...),
    sex: int = Form(...),
    cp: int = Form(...),
    trestbps: float = Form(...),
    chol: float = Form(...),
    fbs: int = Form(...),
    restecg: int = Form(...),
    thalach: float = Form(...),
    exang: int = Form(...),
    oldpeak: float = Form(...),
    slope: int = Form(...),
    ca: float = Form(...),
    thal: float = Form(...)
):
    try:
        features = pd.DataFrame([[age, sex, cp, trestbps, chol, fbs, restecg,
                                   thalach, exang, oldpeak, slope, ca, thal]],
                                columns=FEATURE_NAMES)
        features_processed = preprocessor.transform(features)
        prediction = int(model.predict(features_processed)[0])
        probability = float(model.predict_proba(features_processed)[0, 1])

        return templates.TemplateResponse("index.html", {
            "request": request,
            "prediction": "Heart Disease Detected" if prediction == 1 else "No Heart Disease",
            "probability": f"{probability * 100:.1f}%",
            "risk": "High" if probability > 0.7 else "Moderate" if probability > 0.3 else "Low",
            "values": {
                "age": age, "sex": sex, "cp": cp, "trestbps": trestbps,
                "chol": chol, "fbs": fbs, "restecg": restecg, "thalach": thalach,
                "exang": exang, "oldpeak": oldpeak, "slope": slope, "ca": ca, "thal": thal
            }
        })
    except Exception as e:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "error": str(e)
        })

@app.get("/health")
async def health():
    return {"status": "ok", "message": "API is running"}

@app.get("/docs")
async def get_docs():
    return {"message": "API documentation available at /docs (Swagger) or /redoc"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)