<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=700&size=28&duration=3000&pause=1000&color=009688&center=true&vCenter=true&width=600&lines=%F0%9F%9A%80+Heart+Disease+Prediction+API;FastAPI+%2B+REST+Endpoints;Production-Ready+Deployment" alt="Heart Disease API" />

<br>

<img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white&labelColor=1a1a2e">
<img src="https://img.shields.io/badge/FastAPI-0.110+-009688?style=for-the-badge&logo=fastapi&logoColor=white&labelColor=1a1a2e">
<img src="https://img.shields.io/badge/Swagger-UI-85EA2D?style=for-the-badge&logo=swagger&logoColor=white&labelColor=1a1a2e">
<img src="https://img.shields.io/badge/Model-scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white&labelColor=1a1a2e">
<img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge&labelColor=1a1a2e">

<br>

<img src="https://github-readme-stats.vercel.app/api?username=basitali08&show_icons=true&theme=radical&hide_border=true&count_private=true" width="400">

</div>

---

## Features

- **Interactive HTML Form** — Test predictions in your browser
- **JSON REST API** — Programmatic access for integration
- **Swagger UI + ReDoc** — Auto-generated API documentation
- **Real-time Inference** — Sub-second predictions
- **Health Check** — Monitoring endpoint

---

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Web interface |
| `/predict` | POST | Form-based prediction |
| `/predict?...` | GET | Programmatic JSON |
| `/health` | GET | Service health check |
| `/docs` | GET | Swagger UI |
| `/redoc` | GET | ReDoc documentation |

---

## Quick Start

```bash
pip install -r requirements.txt
python app/main.py
# Open http://localhost:8000
```

---

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

---

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

---

## Deployment Options

| Platform | Method |
|----------|--------|
| **Local** | `python app/main.py` |
| **Render** | Deploy from GitHub |
| **Hugging Face Spaces** | FastAPI Docker space |
| **Railway/Azure/AWS** | Containerized deployment |

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.9+ | Core language |
| FastAPI | High-performance web framework |
| Scikit-learn | ML model inference |
| Swagger UI | API documentation |
| Jinja2 | HTML templates |

---

<div align="center">

**Built with Python, FastAPI, Scikit-learn**

[![GitHub stars](https://img.shields.io/github/stars/basitali08/heart-disease-api?style=social)](https://github.com/basitali08/heart-disease-api)
[![GitHub forks](https://img.shields.io/github/forks/basitali08/heart-disease-api?style=social)](https://github.com/basitali08/heart-disease-api)

</div>

---

<p align="center">
<b>Built by Basit Ali</b> · <a href="https://github.com/basitali08">GitHub</a> · <a href="mailto:whoisbasit@gmail.com">Email</a><br>
<sub>Healthcare API & Deployment · MS Data Science Portfolio</sub>
</p>