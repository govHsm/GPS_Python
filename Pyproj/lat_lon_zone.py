import pyproj
import math
import time

f = open('HWR.05241059.Nav.txt',encoding='UTF-8') # 텍스트 파일 열기
i = 0
nmea_value = f.readlines() # 파일을 한 줄 씩 리스트 형식으로 받아옴

# GPGGA 위도 ddmm.mmmm 경도 dddmm.mmmm
def converter(lat,lon): # 도,분을 도로 바꿔주는 식
    lat_d = int(lat[:2]) 
    lat_m = float(lat[2:])
    a = lat_m / 60
    aa = lat_d + a

    lon_d = int(lon[0:3]) 
    lon_m = float(lon[3:])
    b = lon_m / 60
    bb = lon_d + b
    return aa, bb

# UTM 존 구하는 공식
def zone(lon):
    zone = ((math.floor(lon) + 180) // 6) + 1
    return zone

# 좌표계 구하는 공식
def Utm(utm_zone,lat,lon,is_nor):
    if is_nor == 'N': # 북인지 남인지
        is_nor = True
    else:
        is_nor = False
    utm_proj = pyproj.Proj(proj="utm", zone=utm_zone, north=is_nor, ellps="WGS84")
    utm_easting, utm_northing = utm_proj(lon, lat)
    return round(utm_easting,2),round(utm_northing,2)

# 좌표만 바꿔주는 파일 쓰기
# def file_write(l_spilt,U_e, U_n):
#     l_spilt[3] = U_e
#     l_spilt[5] = U_n
#     l_s = ','.join(map(str,l_spilt))
#     now = time.strftime('%y%m%H')
#     a = open(f'{now}.txt',"a")
#     a.write(l_s)
#     a.close()


# 리스트에 값을 넣고 파일에 쓰기
def file_write(val_split,U_e,U_n):
    a = []
    a.append(val_split[0])
    a.append(ttime(val_split))
    a.append(U_e)
    a.append(U_n)
    assa = ','.join(map(str,a))
    now = time.strftime('%y%m%H')
    aa = open(f'{now}.txt','a')
    aa.write(assa+'\n')
    aa.close()

# 그리니치 표준 시간대 에서 한국 시간으로 바꿔줌
def ttime(val_split):
    a = val_split[2]
    if a[:2] == 15:
        a[:2] = 00
    f_a = a.find('.')
    return a[:f_a+3]
        

while len(nmea_value) != i: #
    try:
        value = nmea_value[i] # i 라인의 텍스트 값을 받아옴
        val_split = value.split(',') # , 단위로 나눠줌
        lat = val_split[3] # 위도(도,분)
        n_s = val_split[4] # 남,북
        lon = val_split[5] # 경도(도,분)
        la,lo = converter(lat,lon) #  단위로 변환
        U_zone = zone(lo) # 존 구하는 공식(존은 경도로 구함)
        U_e,U_n = Utm(U_zone,la,lo,n_s) # UTM Easting, UTM Northing
        file_write(val_split,U_e,U_n)
        # la -> 위도, lo -> 경도,n_s -> 남,북 구분, U_e -> eas , U_n -> nor
        i += 1
    except Exception as e:
        print(f'오류 발생 : {e}')
f.close() # 파일은 꼭 닫아줘야 함