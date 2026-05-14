from celery import shared_task
from time import sleep
from datetime import timedelta
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)


@shared_task
def send_email():
    sleep(3)
    logger.info("📧 Email sent successfully")
    return {"status": "sent", "timestamp": timezone.now().isoformat()}


@shared_task
def cleanup_old_task_results():

    from django_celery_results.models import TaskResult

    deleted_count, _ = TaskResult.objects.filter(
        status="SUCCESS"
    ).delete()

    return f'{deleted_count} successful tasks cleaned up'