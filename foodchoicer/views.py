from django.shortcuts import render
# from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from group_buying_service.API.weather import request_weather_data
from group_buying_service.API.openAI import request_gpt_response
from datetime import datetime

# Create your views here.

BASE_MESSAGE = [
    {
        "role": "system",
        "content": """
        오늘의 날씨와 시간을 너에게 전달해 줄거야. 그 데이터를 기반으로 적절한 음식을 추천해줘.
        추천해줘야하는 메뉴는 총 5개야.
        """
    }
]


@api_view(['GET'])
def food_choicer(request):

    today = datetime.today()
    lat = float(request.GET.get('lat'))
    lon = float(request.GET.get('lon'))

    # print(lat, lon, type(lat), type(lon))

    weather_data = request_weather_data(lat, lon)

    gpt_prompt = f"오늘은 {today}야. 오늘의 날씨는 다음과 같아. "

    for key, value in weather_data.items():
        gpt_prompt += f'{key}은(는) {value}. '

    gpt_prompt += "적절한 메뉴를 추천해줘."

    gpt_response = request_gpt_response(BASE_MESSAGE, gpt_prompt)

    return Response({"message": gpt_response}, status=status.HTTP_200_OK)


def index(request):
    return render(request, "foodchoicer/index.html")









