from math import pi, log, cos, tan, sin, floor
from rest_framework.views import APIView

# Create your views here.


COEFFICIENT_TO_RADIAN = pi / 180.0
GRID_UNIT_COUNT = 6371.00877 / 5.0  #지구 반지름 ÷ 정방형 격자 단위 길이 = 격자 개수
REF_X = 43.0 # 기준점 X좌표
REF_Y = 136.0 # 기준점 Y좌표
REF_LON_RAD = 126.0 * COEFFICIENT_TO_RADIAN # 기준점 경도 (rad)
REF_LAT_RAD = 38.0 * COEFFICIENT_TO_RADIAN # 기준점 위도 (rad)
PROJ_LAT_1_RAD = 30.0 * COEFFICIENT_TO_RADIAN # 투영 위도1 (rad)
PROJ_LAT_2_RAD = 60.0 * COEFFICIENT_TO_RADIAN # 투영 위도2 (rad)

sn = log(cos(PROJ_LAT_1_RAD) / cos(PROJ_LAT_2_RAD)) / log(tan(pi * 0.25 + PROJ_LAT_2_RAD * 0.5) / tan(pi * 0.25 + PROJ_LAT_1_RAD * 0.5))
sf = tan(pi * 0.25 + PROJ_LAT_1_RAD * 0.5)**(sn) * cos(PROJ_LAT_1_RAD) / sn
ro = GRID_UNIT_COUNT * sf / tan(pi * 0.25 + REF_LAT_RAD * 0.5)**(sn)

def convertToXy(lat, lon):
    ra = GRID_UNIT_COUNT * sf / tan(pi * 0.25 + lat * COEFFICIENT_TO_RADIAN * 0.5)**(sn)
    theta = lon * COEFFICIENT_TO_RADIAN - REF_LON_RAD
    if (theta < -pi):
        niceTheta = theta + 2 * pi
    elif (theta > pi) :
        niceTheta = theta - 2 * pi
    else:
        niceTheta =  theta

    nx = int(floor(ra * sin(niceTheta * sn) + REF_X + 0.5))
    ny = int(floor(ro - ra * cos(niceTheta * sn) + REF_Y + 0.5))

    return (nx, ny)
