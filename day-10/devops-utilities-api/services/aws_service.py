"""
AWS helper utilities.

Note:
- This module assumes AWS credentials are configured (env vars, AWS profile, IAM role, etc.)
- Keep it framework-agnostic (no FastAPI objects here).
"""

from __future__ import annotations

from datetime import datetime, timezone, timedelta
from typing import Dict, Any, List

import boto3


def get_bucket_info(days_threshold: int = 90) -> Dict[str, Any]:
    """
    Fetch S3 bucket inventory and categorize buckets by age.

    Args:
        days_threshold: Buckets older than this many days are marked as "old".

    Returns:
        Dict with counts and bucket name lists.
    """
    s3_client = boto3.client("s3")

    buckets = s3_client.list_buckets().get("Buckets", [])
    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(days=days_threshold)

    new_buckets: List[str] = []
    old_buckets: List[str] = []

    for bucket in buckets:
        name = bucket.get("Name")
        created = bucket.get("CreationDate")

        if not name or not created:
            continue

        # boto3 typically returns timezone-aware datetimes; normalize to UTC
        if created.tzinfo is None:
            created = created.replace(tzinfo=timezone.utc)

        if created < cutoff:
            old_buckets.append(name)
        else:
            new_buckets.append(name)

    return {
        "total_buckets": len(new_buckets) + len(old_buckets),
        "new_buckets": len(new_buckets),
        "old_buckets": len(old_buckets),
        "new_bucket_names": new_buckets,
        "old_bucket_names": old_buckets,
        "days_threshold": days_threshold,
    }
