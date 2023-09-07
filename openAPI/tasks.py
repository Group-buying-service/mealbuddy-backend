from mealbuddy.celery import app
from celery import shared_task
from .foodchoicer_prompt import flush_prompt, set_prompt, get_prompt

@app.task
def flush_prompt_task():
    flush_prompt()
    return "flushed_chatGPT_prompt"