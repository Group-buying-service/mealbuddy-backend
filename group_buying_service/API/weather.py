import requests
import json
from datetime import datetime 
from decouple import config
from group_buying_service.utils.coordinate_convert import convertToXy 

weather_API_url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst'
weather_API_key = config('WEATHER_API_KEY')


def convert_hour(hour):
    past_hours = [2, 5, 8, 11, 14, 17, 20, 23]
    
    nearest_past_hour = max(filter(lambda x: x <= int(hour), past_hours))
    
    return str(nearest_past_hour)+'00'


def get_weather_data(items):

    weather_data = {}

    for item in items['item']:

        match item['category']:
            case 'PTY':
                weather_code = item['fcstValue']
                match weather_code:
                    case '1':
                        weather_state = '비'
                    case '2':
                        weather_state = '비/눈'
                    case '3':
                        weather_state = '눈'
                    case '4':
                        weather_state = '소나기'
                    case _:
                        weather_state = '없음'
                weather_data['강수형태'] = weather_state
            case 'SKY':
                weather_code = item['fcstValue']
                match weather_code:
                    case '1':
                        weather_state = '맑음'
                    case '3':
                        weather_state = '구름많음'
                    case '4':
                        weather_state = '흐림'
                    case _:
                        weather_state = '그 외'
                weather_data['날씨'] = weather_state
            case 'PCP':
                weather_data['강수량'] = item['fcstValue'] + 'mm' if item['fcstValue'].isdigit() else item['fcstValue'] 
            case 'TMP':
                weather_data['기온'] = item['fcstValue'] + '℃'
            case 'REH':
                weather_data['습도'] = item['fcstValue'] + '%'
            case 'WSD':
                weather_data['풍속'] = item['fcstValue'] + 'm/s'
            case _:
                pass
    return weather_data

def request_weather_data(lat, lon, basedate = None, time = None, pageNo=1, numOfRows = 12):

    if not basedate and not time:
        today = datetime.today()
        base_date = today.strftime("%Y%m%d")
        time = today.strftime("%H")
    base_time = convert_hour(time)
    nx, ny = convertToXy(lat,lon)

    payload = f"?serviceKey={weather_API_key}&numOfRows={numOfRows}&pageNo={pageNo}&dataType=json&base_date={base_date}&base_time={base_time}&nx={nx}&ny={ny}"

    res = requests.get(weather_API_url + payload)

    items = res.json().get('response').get('body').get('items')

    return get_weather_data(items)
