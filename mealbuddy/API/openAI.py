from decouple import config

import openai
import json

openai.api_key = config('OPENAI_API_KEY')


def request_gpt_response(messages:list):

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = messages,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )
    except Exception as e:
        return False

    response = response.choices[0]['message']['content'].strip()

    messages.append({"role":"assistant", "content": response})

    return messages