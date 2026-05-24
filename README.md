# 🚀 Heart Disease Prediction API — FastAPI Deployment

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688?logo=fastapi)](https://fastapi.tiangolo.com)
[![Swagger](https://img.shields.io/badge/Swagger-UI-85EA2D?logo=swagger)](https://swagger.io)
[![scikit-learn](https://img.shields.io/badge/Model-scikit--learn-F7931E?logo=scikit-learn)](https://scikit-learn.org)

Production-ready REST API serving heart disease predictions using a trained ML model. Built with **FastAPI** for high performance, automatic OpenAPI docs, and interactive testing.

---

## Features

- **Interactive HTML Form** — Test predictions in your browser
- **JSON REST API** — Programmatic access for integration
- **Swagger UI + ReDoc** — Auto-generated API documentation
- **Real-time Inference** — Sub-second predictions
- **Health Check** — Monitoring endpoint

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Web interface |
| `/predict` | POST | Form-based prediction |
| `/predict?...` | GET | Programmatic JSON |
| `/health` | GET | Service health check |
| `/docs` | GET | Swagger UI |
| `/redoc` | GET | ReDoc documentation |

## Quick Start

```bash
pip install -r requirements.txt
python app/main.py
# Open http://localhost:8000
```

## API Usage

```python
import requests
r = requests.get("http://localhost:8000/predict", params={
    "age": 52, "sex": 1, "cp": 0, "trestbps": 130,
    "chol": 240, "fbs": 0, "restecg": 1, "thalach": 150,
    "exang": 0, "oldpeak": 1.0, "slope": 1, "ca": 0, "thal": 1
})
print(r.json())
# {"prediction": 0, "prediction_text": "No Heart Disease", ...}
```

## Project Structure

```
heart-disease-api/
├── app/
│   └── main.py           # FastAPI application
├── models/                # Trained ML model
├── templates/
│   └── index.html         # Web interface
├── requirements.txt
└── README.md
```

## Deployment Options

| Platform | Method |
|----------|--------|
| **Local** | `python app/main.py` |
| **Render** | Deploy from GitHub |
| **Hugging Face Spaces** | FastAPI Docker space |
| **Railway/Azure/AWS** | Containerized deployment |

---

<p align="center">
<b>Built by Basit Ali</b> · <a href="https://github.com/basitali08">GitHub</a> · <a href="mailto:whoisbasit@gmail.com">Email</a>
</p>
