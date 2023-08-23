import requests
import json
from datetime import datetime 
from decouple import config
from foodchoicer.utils.coordinate_convert import convertToXy 

URL = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst'
KEY = config('WEATHER_API_KEY')

def convert_hour(hour):
    past_hours = [2, 5, 8, 11, 14, 17, 20, 23]
    
    nearest_past_hour = max(filter(lambda x: x <= int(hour), past_hours))
    
    return str(nearest_past_hour)+'00'

def get_weather_data(lat, lon):

    today = datetime.today()
    base_date = today.strftime("%Y%m%d")
    base_time = convert_hour(today.strftime("%H"))
    nx, ny = convertToXy(lat,lon)

    payload = f"?serviceKey={KEY}&numOfRows=12&pageNo=1&dataType=json&base_date={base_date}&base_time={base_time}&nx={nx}&ny={ny}"

    res = requests.get(URL + payload)

    items = res.json().get('response').get('body').get('items')

    return items
