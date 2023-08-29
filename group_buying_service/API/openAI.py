from decouple import config

import openai
import json

openai.api_key = config('OPENAI_API_KEY')


def request_gpt_response(base_message, string):
    
    messages = base_message[:]
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