from decouple import config

import openai
import json

openai.api_key = config('OPENAI_API_KEY')

BASE_MESSAGE = [
    {
        "role": "system",
        "content": """
        오늘의 날씨와 시간을 너에게 전달해 줄거야. 그 데이터를 기반으로 적절한 음식을 추천해줘.
        추천해줘야하는 메뉴는 총 5개야.
        """
    }
]


def request_gpt_response(string):
    
    messages = BASE_MESSAGE[:]
    messages.append({"role": "user", "content": string})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = messages,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=1.0,
    )

    response = response.choices[0]['message']['content'].strip()

    return response