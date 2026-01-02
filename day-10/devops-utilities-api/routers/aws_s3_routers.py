"""
AWS S3 routes.

Thin router layer:
- validate input
- call AWS service
- return response
"""

from fastapi import APIRouter, HTTPException, Query
from starlette import status

from services.aws_service import get_bucket_info

router = APIRouter()


@router.get("/s3", status_code=status.HTTP_200_OK)
def list_s3_buckets(days_threshold: int = Query(90, ge=1, le=3650)) -> dict:
    """
    Return basic S3 bucket inventory.

    Optional query params:
        days_threshold: age cutoff in days to classify "old" buckets.
    """
    try:
        return {"buckets": get_bucket_info(days_threshold=days_threshold)}
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to fetch S3 bucket info: {exc}",
        )
