"""
Metrics routes.

Thin router layer:
- validate input
- call service layer
- return response
"""

from fastapi import APIRouter, HTTPException, Query
from starlette import status

from services.metrics_service import get_system_metrics

router = APIRouter()


@router.get("/metrics", status_code=status.HTTP_200_OK)
def get_metrics(cpu_threshold: float = Query(10.0, ge=0.0, le=100.0)) -> dict:
    """
    Return system metrics.

    Optional query params:
        cpu_threshold: threshold used to label system_status (0-100).
    """
    try:
        return get_system_metrics(cpu_threshold=cpu_threshold)
    except Exception as exc:
        # In production you'd log the exception with stacktrace
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to fetch system metrics: {exc}",
        )
