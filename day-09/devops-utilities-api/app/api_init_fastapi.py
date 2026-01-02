from fastapi import FastAPI  # fastapi = library, FastAPI = class

from routers.metrics import router as metrics_router

from routers.aws_s3_routers import router as aws_s3_router
#from routers import aws_s3_routers as aws_s3_routers

# FastAPI creates an application object that converts Python functions into API endpoints
app = FastAPI(
    title="Internal DevOps Utilities API",
    description="Internal DevOps API for monitoring system metrics, AWS usage, log analysis, etc.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

@app.get("/")  # Registers this function as a GET endpoint for "/"
def hello():
    """
    Root endpoint for testing the API.
    """
    return {
        "message": "Hello Doston, This is the DevOps Utilities API"
    }

# Register metrics routes
app.include_router(metrics_router)
app.include_router(aws_s3_router, prefix="/aws")
#app.include_router(aws_s3_routers)
