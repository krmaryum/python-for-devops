from fastapi import APIRouter, HTTPException
from starlette import status

from services.aws_service import get_bucket_info

router = APIRouter()

@router.get("/s3", status_code=status.HTTP_200_OK)
def get_buckets():
    try:
        buckets_info = get_bucket_info()
        return {"buckets": buckets_info}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
