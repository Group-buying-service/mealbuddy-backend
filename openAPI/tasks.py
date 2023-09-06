from __future__ import absolute_import
from group_buying_service.celery import app
from .foodchoicer_prompt import chatGPT_prompt_redis_client

@app.task
def flush_prompt():
    print("hello")
    chatGPT_prompt_redis_client.flushdb()