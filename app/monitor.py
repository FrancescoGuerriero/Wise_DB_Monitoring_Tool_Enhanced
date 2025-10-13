import psutil
from datetime import datetime
from app.db import SessionLocal, ServerMetrics, Alerts

CPU_THRESHOLD = 80.0
MEM_THRESHOLD = 80.0
DISK_THRESHOLD = 90.0

def collect_metrics():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    return {"cpu": cpu, "memory": memory, "disk": disk, "timestamp": datetime.utcnow()}

def save_metrics():
    session = SessionLocal()
    metrics = collect_metrics()

    # Save metrics
    metric_record = ServerMetrics(cpu=metrics["cpu"], memory=metrics["memory"], disk=metrics["disk"])
    session.add(metric_record)

    # Check thresholds for alerts
    if metrics["cpu"] > CPU_THRESHOLD:
        session.add(Alerts(server_name="local_server", alert_type="CPU", description=f"CPU usage high: {metrics['cpu']}%"))
    if metrics["memory"] > MEM_THRESHOLD:
        session.add(Alerts(server_name="local_server", alert_type="Memory", description=f"Memory usage high: {metrics['memory']}%"))
    if metrics["disk"] > DISK_THRESHOLD:
        session.add(Alerts(server_name="local_server", alert_type="Disk", description=f"Disk usage high: {metrics['disk']}%"))

    session.commit()
    session.close()
