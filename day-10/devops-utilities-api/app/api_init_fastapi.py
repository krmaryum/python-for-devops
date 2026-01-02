"""
FastAPI application factory / initialization.

This app exposes internal DevOps utilities such as:
- system metrics (CPU, memory, disk)
- AWS helpers (S3 bucket inventory)

Keep this file focused on app wiring (routers, middleware, metadata).
Business logic belongs in services/.
"""

from fastapi import FastAPI

from routers.metrics import router as metrics_router
from routers.aws_s3_routers import router as aws_s3_router

app = FastAPI(
    title="Internal DevOps Utilities API",
    description="Internal DevOps API for monitoring system metrics and basic AWS utilities.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

@app.get("/", tags=["health"])
def health_check() -> dict:
    """Simple health endpoint to verify the API is running."""
    return {"status": "ok", "message": "DevOps Utilities API is running"}

# Register routers
app.include_router(metrics_router, tags=["metrics"])
app.include_router(aws_s3_router, prefix="/aws", tags=["aws"])
