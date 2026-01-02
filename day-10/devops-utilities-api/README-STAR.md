# DevOps Utilities API (FastAPI Capstone)

## Overview
This project is a DevOps-focused automation service built with FastAPI.
It exposes system health metrics such as CPU, memory, and disk usage through HTTP endpoints, transforming Python automation into a reusable and scalable operational tool.

The goal of this project is to demonstrate how DevOps engineers operationalize scripts for real-world production use.

---

## DevOps Problem Context
In production environments, system health checks are critical for stability and reliability.
However, manually checking CPU, memory, and disk usage does not scale and can delay issue detection.

This project addresses that gap by automating metrics collection and exposing it in a standardized way.

---

## Features
- API-based access to system metrics (CPU, memory, disk)
- Python automation wrapped using FastAPI
- Clean separation of API and business logic
- Basic validation and error handling
- Designed as an internal DevOps utility service

---

## Technology Stack
- Python
- FastAPI
- Uvicorn
- psutil

---

## Project Structure
```
devops-utilities-api/
├── app/
│   └── api_init_fastapi.py
├── routers/
│   └── metrics.py
├── services/
│   └── metrics_service.py
├── main_entry_pt_execute.py
├── requirements.txt
└── README.md
```

---

## How to Run

### Create virtual environment
```bash
python -m venv venv
.\venv\Scripts\Activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Start the API
```bash
python main_entry_pt_execute.py
```

### Access API
- Swagger UI: http://127.0.0.1:8000/docs
- Metrics endpoint: /metrics

---

## STAR Explanation – Capstone Project

### Situation
- System health metrics like CPU, memory, and disk usage were being checked manually.
- Manual monitoring is time-consuming and does not scale in production environments.

### Task
- Automate the collection of system metrics.
- Expose the automation in a reusable and standardized way.

### Action
- Implemented Python automation using psutil to collect system metrics.
- Structured the project with a service layer for maintainability.
- Built a FastAPI wrapper to expose metrics via HTTP endpoints.
- Added basic validation and error handling for reliable execution.

### Result
- System metrics can now be accessed programmatically via an API.
- Reduced manual effort for monitoring.
- Automation is reusable and easy to integrate with other tools.
- Demonstrated core DevOps principles: automation, reliability, and observability.

---

## Key Learnings
- Python is a powerful enabler for DevOps automation.
- Converting scripts into services improves reliability and reuse.
- DevOps is about ownership, clarity, and operational thinking.
