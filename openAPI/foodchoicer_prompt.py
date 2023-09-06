import redis
import json
from datetime import timedelta, datetime
from decouple import config
from group_buying_service.API.weather import request_weather_data
from group_buying_service.celery import app


chatGPT_prompt_redis_client = redis.StrictRedis(host=config('REDIS_HOST'), port=config('REDIS_PORT'), db=1)

BASE_MESSAGE = [
    {
        "role": "system",
        "content": """
        assistant는 날씨와 시간을 바탕으로 식사 메뉴를 추천해주는 전문가야.
        오늘의 날씨와 시간을 assistant에게 전달해 줄거야. 그 데이터를 기반으로 적절한 음식을 추천해 줘.
        추천해줘야하는 메뉴는 기본적으로 5개야.
        """
    }
]

def init_prompt(lat, lon, message):

    prompt = BASE_MESSAGE[:]

    weather_data = request_weather_data(lat, lon)
    today = datetime.today()

    if weather_data:
        message = f"오늘은 {today}야. 오늘의 날씨는 다음과 같아."

        for key, value in weather_data.items():
            message += f'{key}은(는) {value}. '

        message += "적절한 메뉴를 추천해줘."
    
        prompt.append({"role":"user", "message": message})

        return prompt
    return False

def reset_prompt(user_id):
    chatGPT_prompt_redis_client.delete(f'chatgpt_prompt_{user_id}')

def get_prompt(user_id):
    result = chatGPT_prompt_redis_client.get(f'chatgpt_prompt_{user_id}')
    return json.loads(result) if result else None

def set_prompt(user_id, message:list):
    chatGPT_prompt_redis_client.setex(f'chatgpt_prompt_{user_id}', 3600, json.dumps(message))





