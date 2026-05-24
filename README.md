# Heart Disease Prediction API

## Overview
Production-ready REST API for heart disease prediction using a trained machine learning model. Built with FastAPI for high performance and automatic documentation.

## Features
- **Web Interface**: Interactive HTML form for easy testing
- **JSON API**: RESTful endpoint for programmatic access
- **Auto Documentation**: Swagger UI and ReDoc
- **Real-time Predictions**: Instant risk assessment
- **Health Check**: Monitoring endpoint

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Web interface |
| `/predict` | POST | Form-based prediction |
| `/predict?age=52&sex=1&...` | GET | JSON prediction |
| `/health` | GET | Health check |
| `/docs` | GET | Swagger UI |
| `/redoc` | GET | ReDoc documentation |

## Quick Start
```bash
pip install -r requirements.txt
python app/main.py
```

Then open http://localhost:8000 in your browser.

## API Usage Example
```python
import requests

params = {
    "age": 52, "sex": 1, "cp": 0, "trestbps": 130,
    "chol": 240, "fbs": 0, "restecg": 1, "thalach": 150,
    "exang": 0, "oldpeak": 1.0, "slope": 1, "ca": 0, "thal": 1
}

response = requests.get("http://localhost:8000/predict", params=params)
print(response.json())
# Output: {"prediction": 0, "prediction_text": "No Heart Disease", ...}
```

## Project Structure
```
heart-disease-api/
├── app/
│   └── main.py           # FastAPI application
├── models/                # Trained ML model artifacts
├── templates/
│   └── index.html         # Web interface
├── requirements.txt
└── README.md
```

## Deployment Options
- **Local**: `python app/main.py`
- **Docker**: Containerize with Dockerfile
- **Cloud**: Deploy to Heroku, AWS, GCP, or Azure
- **Platform**: Render, Railway, or Hugging Face Spaces
