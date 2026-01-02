# DevOps Utilities API 

A FastAPI-based **Internal DevOps Utilities API** designed to expose system metrics, AWS utilities, and operational endpoints useful for DevOps engineers, SREs, and platform teams.

---

##  Features

-  System metrics (CPU, Memory, Disk, etc.)
-  AWS utility endpoints (S3, future AWS services)
- High-performance FastAPI framework
- Auto-generated API documentation (Swagger & ReDoc)
- Modular architecture using routers and services
-  DevOps-friendly & Docker-ready structure

---

##  Project Structure

```
devops-utilities-api/
├── app/
│   └── api_init_fastapi.py     # FastAPI application initialization
├── routers/
│   ├── metrics.py              # Metrics API routes
│   └── aws_s3_routers.py       # AWS S3 related routes
├── services/
│   ├── metrics_service.py      # Business logic for system metrics
│   └── aws_service.py          # AWS service logic
├── fastapi/                    # Virtual environment (venv)
├── main_entry_pt_execute.py    # Application entry point
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## Tech Stack

- **Language:** Python 3
- **Framework:** FastAPI
- **ASGI Server:** Uvicorn
- **Cloud SDK:** boto3 (AWS)
- **Monitoring:** System metrics via Python utilities
- **Docs:** Swagger UI & ReDoc

---

## Setup & Installation

### 1️⃣ Create the project folder
```bash
cd devops-utilities-api
```

### 2️⃣ Create & activate virtual environment
```bash
python -m venv fastapi
source fastapi/bin/activate   # Linux/Mac
fastapi\Scripts\Activate.ps1    # Windows
```

### 3️⃣ Install dependencies via requirements.txt
```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

### Recommended (CLI)
```bash
python main_entry_pt_execute.py
```

### Using entry point
```bash
python main_entry_pt_execute.py
```

---

##  API Endpoints

| Method | Endpoint | Description |
|------|--------|-------------|
| GET | `/` | Root test endpoint |
| GET | `/metrics` | System metrics |
| GET | `/docs` | Swagger UI |
| GET | `/redoc` | ReDoc UI |

---

##  API Documentation

- Swagger UI → http://127.0.0.1:8000/docs
- ReDoc → http://127.0.0.1:8000/redoc

---

##  Use Cases

- Internal monitoring tools
- DevOps automation APIs
- Learning FastAPI + DevOps
- Interview & portfolio project

---

##  Future Enhancements

- Prometheus `/metrics` format
- Authentication & authorization
- Docker & Kubernetes deployment
- CI/CD integration
- More AWS service APIs

---

##  TrainWithShubham
Thanks, Shubham Bhaeya!!

Built as part of a **DevOps learning & utilities project** using FastAPI From TrainWithShubham.


