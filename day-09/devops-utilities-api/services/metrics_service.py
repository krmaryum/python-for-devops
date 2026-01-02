import psutil


def get_system_metrics():
    """
    This API get the System Metrics(CPU, Memory, Disk, CPU Utilization)
    Base on a CPU Threshold i.e. 10 (Configurable)
    """
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage('/').percent


    cpu_threshold = 10
    #if cpu_percent > cpu_threshold:
    #    status = 'CPU Utilization: High'
    #else:
    #    status = 'CPU Utilization: Low'
    status = "CPU Utilization: High" if cpu_percent > cpu_threshold else "CPU Utilization: Low"


    return {
        'cpu_percent': cpu_percent,
        'memory_percent': memory_percent,
        'disk_percent': disk_percent,
        'cpu_threshold': cpu_threshold,
        'system_status': status
    }