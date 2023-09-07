from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework import status
from group_buying_service.API.weather import request_weather_data
from group_buying_service.API.openAI import request_gpt_response
from datetime import datetime
from .foodchoicer_prompt import get_prompt, set_prompt, init_prompt, reset_prompt, get_throttle, increase_throttle

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


@api_view(['POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def food_choicer(request):

    if request.method == 'POST':
        user = request.user
        lat = float(request.data.get('lat', 0))
        lon = float(request.data.get('lon', 0))
        message = request.data.get('message')

        throttle = get_throttle(user.id)
        if throttle == 'Too many request':
            return Response("하루에 10번만 질문할 수 있습니다.", status=status.HTTP_429_TOO_MANY_REQUESTS)

        prompt = get_prompt(user.id)
        
        if prompt:
            prompt.append({"role":"user", "content": message})
        else:
            prompt = init_prompt(lat, lon)
            if prompt:
                prompt.append({"role":"user", "content": message})
            else:
                return Response("예기치 않은 오류가 발생했습니다.", status=status.HTTP_408_REQUEST_TIMEOUT)
        
        response = request_gpt_response(prompt)

        if response:
            set_prompt(user.id, response)
            increase_throttle(user.id, throttle)
            return Response(response, status=status.HTTP_200_OK)
        return Response("예기치 않은 오류가 발생했습니다.", status=status.HTTP_408_REQUEST_TIMEOUT)
    
    if request.method == 'DELETE':
        user = request.user
        reset_prompt(user.id)
        return Response('대화내역이 초기화 되었습니다.', status=status.HTTP_200_OK)

@api_view(['GET'])
def check(request):

    user = request.user
    prompt = get_prompt(user.id)

    return Response({"test":prompt})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def weather(request):

    lat = float(request.GET.get('lat'))
    lon = float(request.GET.get('lon'))

    weather_data = request_weather_data(lat, lon)
    if weather_data:
        return Response(weather_data, status=status.HTTP_200_OK)
    return Response("예기치 않은 오류가 발생했습니다.", status=status.HTTP_408_REQUEST_TIMEOUT)








