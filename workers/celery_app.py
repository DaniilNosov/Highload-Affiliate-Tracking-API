from celery import Celery
from core.config import settings

celery_app = Celery(
    "cpa_tasks",
    broker=settings.redis_url,
    include=["workers.tasks"]
)
