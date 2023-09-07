from celery import Celery
from celery.schedules import crontab
from django.conf import settings
from decouple import config
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'group_buying_service.settings')

app = Celery(
    'group_buying_service',
    broker = f'redis://{config("REDIS_HOST")}:{config("REDIS_PORT")}/10',
    )

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'flush-prompt-every-midnight': {
        'task': 'openAPI.tasks.flush_prompt_task',
        'schedule': crontab(hour=4),
    },
}