"""
System metrics collection.

This module contains pure-Python logic (no FastAPI code).
That keeps the service testable and reusable.
"""

from __future__ import annotations

from typing import Dict, Any

import psutil

DEFAULT_CPU_THRESHOLD = 10.0  # percent


def get_system_metrics(cpu_threshold: float = DEFAULT_CPU_THRESHOLD) -> Dict[str, Any]:
    """
    Collect basic system metrics.

    Args:
        cpu_threshold: CPU percent threshold used to label system_status.

    Returns:
        Dict with cpu_percent, memory_percent, disk_percent, cpu_threshold, and system_status.
    """
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage("/").percent

    system_status = "CPU Utilization: High" if cpu_percent > cpu_threshold else "CPU Utilization: Normal"

    return {
        "cpu_percent": cpu_percent,
        "memory_percent": memory_percent,
        "disk_percent": disk_percent,
        "cpu_threshold": cpu_threshold,
        "system_status": system_status,
    }
