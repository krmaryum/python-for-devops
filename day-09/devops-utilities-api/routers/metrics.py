from fastapi import APIRouter, HTTPException
from starlette import status

from services.metrics_service import get_system_metrics as fetch_system_metrics

router = APIRouter()

@router.get("/metrics", status_code=status.HTTP_200_OK)
def get_metrics():
    try:
        return fetch_system_metrics()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
