import pyproj # 지리적 좌표 변환을 수행하기 위한 라이브러리
import math
import time

# 변수 수정하기!!

# 끝자리 해결

def nav_change(file_path):
    nav_all = []
    f = open(file_path,encoding='UTF-8') # 텍스트 파일 열기
    while True:
        nav_list = f.readline() # 한 줄 씩 읽어와
        if nav_list == '':
            break
        nav_all += [list(map(float,nav_list.split()))] # 이차원 배열로 추가해줌
    return nav_all

# 큰 거에서 작은 거의 차를 구해서 0의 갯수만큼 나누자

def changeint(nav_all):
    for n in nav_all:
        n[0] = int(n[0])

def change_format(nav_all):
    for n in nav_all:
        n[0] = "%-3d" % n[0]
        n[2] = "%.2f" % n[2]  # 소수점 두 자리까지 표시할 경우
        n[3] = "%.2f" % n[3]  # 소수점 두 자리까지 표시할 경우




# 파일 내부 0이 있는 곳의 차를 구하고 0인 곳에 합쳐줌
def list_sum(c,d,a_a,nav_al):
    cc = 0
    dd = 0
    cc = c[0] - c[1]# 209 - 206
    dd = d[0] - d[1]# 209 - 206
    ccc = round(cc / len(a_a),2)
    ddd = round(dd / len(a_a),2)
    for _ in a_a:
        nav_al[_][2] += round(nav_al[_-1][2] - ccc,2)
        nav_al[_][3] += round(nav_al[_-1][3] - ddd,2)
    return nav_al
    
def same_change(nav_all):
    a = 0
    second_list = []
    third_list = []
    while len(nav_all) != a:
        if a >= 1:
            if a + 1 != len(nav_all):
                if nav_all[a-1][1] == nav_all[a][1] == nav_all[a+1][1]: # 시간이 같고 x 의 좌표가 같을 경우
                    if nav_all[a-1][2] == nav_all[a][2]:
                        second_same = round((nav_all[a+2][2] - nav_all[a][2])/2,2)
                        second_list.append(second_same)
                        nav_all[a][2] = round(nav_all[a+2][2]- second_same,2)
                        nav_all[a+1][2] = round(nav_all[a+2][2]- (second_same*2),2)
                    if nav_all[a-1][3] == nav_all[a][3]: # 시간이 같고 y 의 좌표가 같을 경우
                        third_same = round((nav_all[a+2][3] - nav_all[a][3])/2,2)
                        third_list.append(third_same)
                        nav_all[a][3] = round(nav_all[a+2][3]- third_same,2)
                        nav_all[a+1][3] = round(nav_all[a+2][3]- (third_same*2),2)

                elif nav_all[a-1][1] == nav_all[a][1]: # 시간이 같고 x 의 좌표가 같을 경우
                    if nav_all[a-1][2] == nav_all[a][2]:
                        second_same = round((nav_all[a+1][2] - nav_all[a][2])/2,2)
                        nav_all[a][2] = round(nav_all[a+1][2]- second_same,2)
                        second_list.append(second_same)
                    if nav_all[a-1][3] == nav_all[a][3]: # 시간이 같고 y 의 좌표가 같을 경우
                        third_same = round((nav_all[a+1][3] - nav_all[a][3])/2,2)
                        third_list.append(third_same)
                        nav_all[a][3] = round(nav_all[a+1][3]- third_same,2)
            else:
                if nav_all[a][1] == nav_all[a-1][1]:
                    if nav_all[a][2] == nav_all[a-1][2]:
                        nav_all[a][2] += avg_second(second_list)
                    if nav_all[a][3] == nav_all[a-1][3]:
                        nav_all[a][3] += avg_third(third_list)
        a += 1
                        

        

    # # 시간의 값이 같을 경우 / 수정본
    #     if a >= 2 and nav_all[a-1][1] == nav_all[a-2][1] and nav_all[a-1][2] == nav_all[a-2][2] and nav_all[a-1][3] == nav_all[a-2][3]:
    #         second_same = round((nav_all[a][2] - nav_all[a-1][2]) / 2,2)
    #         third_same = round((nav_all[a][3] - nav_all[a-1][3]) / 2,2)
    #         nav_all[a-1][2] = round(nav_all[a][2] - second_same,2)
    #         nav_all[a-1][3] = round(nav_all[a][3] - third_same,2)
    #     a += 1

def time_change(nav_all):
    a = 0
    while len(nav_all) != a:
        if a >= 1:
            if a + 1 != len(nav_all):
                if nav_all[a][1] == nav_all[a-1][1] == nav_all[a+1][1]: # a가 2이면 a = 1 이나 a = 3
                    nav_all[a-1][1] += 0.3
                    nav_all[a][1] += 0.5
                    nav_all[a+1][1] += 0.8

                elif nav_all[a][1] == nav_all[a-1][1]:
                    nav_all[a][1] += 0.5
            else:
                if nav_all[a][1] == nav_all[a-1][1]:
                    nav_all[a][1] += 0.5
        a += 1
    

        
        

def zeroto(nav_all): # 시간 및 0의 자리 바꿔주는 함수
    a = 0 # nav_all의 리스트 카운트(행)
    b = [] # 
    bb = []
    a_a = [] # 배열 숫자 기억
    while len(nav_all) != a: # 1491

        
        # # 시간의 값이 같을 경우 / 원본
        # if a+3 <= len(nav_all) and nav_all[a][1] == nav_all[a+1][1] and nav_all[a][2] == nav_all[a+1][2] and nav_all[a][3] == nav_all[a+1][3]:
        #     second_same = round((nav_all[a+2][2] - nav_all[a+1][2]) / 2,2)
        #     third_same = round((nav_all[a+2][3] - nav_all[a+1][3]) / 2,2)
        #     nav_all[a+1][2] = round(nav_all[a+2][2] - second_same,2)
        #     nav_all[a+1][3] = round(nav_all[a+2][2] - third_same,2)



        # # 시간 자리 설정, 최대 3자리, 만약 4자리가 나오면 수정해야 함
        # if a+3 <= len(nav_all) and nav_all[a][1] == nav_all[a+1][1] and nav_all[a][1] == nav_all[a+2][1]: # 97 < 100
        #     nav_all[a][1] += 0.3
        #     nav_all[a+1][1] += 0.5
        #     nav_all[a+2][1] += 0.8
        # elif a+3<len(nav_all) and nav_all[a][1] == nav_all[a+1][1]:
        #     nav_all[a+1][1] += 0.5

        if nav_all[a][2] == 0:
            a_a.append(a) # 몇 번 부터 0이었는지 기억해줌
            b += [nav_all[a-1][2]]
            bb += [nav_all[a-1][3]]

            for i in range(1,30): # 최대 공백을 30이라고 생각할 때
                if nav_all[a+i][2] != 0: # 0이 아닐 시
                    b += [nav_all[a+i][2]] # 더해주고
                    bb += [nav_all[a+i][3]] # 더해주고
                    list_sum(b,bb,a_a,nav_all)
                    a += len(a_a)
                    b = []
                    bb = []
                    a_a = []
                    break
                a_a.append(a + i)
        a += 1 # 리스트 카운터


# 파일 생성해주는 기능 , 파일 이름은 시간으로 설정됨
def file_make(file_name,nav_all):
    now = time.strftime('%y.%m.%H.%M.%S'+'_')
    for nn in nav_all:
        strnav = ''
        for nnn in nn:
            strnav += str(nnn) + '    '
        file_change = open(f'{now+file_name}.txt','a')
        file_change.write(strnav+'\n')
        file_change.close

# GPS 이동거리 평균

def avg_second(second_value): # gps x 평균  이동 거리
    second_value_all = 0
    for list_second in second_value:
        second_value_all += list_second
    second_value_all = round(second_value_all / len(second_value),2)
    return second_value_all

def avg_third(third_value): # gps y 평균 이동 거리
    third_value_all = 0
    for list_third in third_value:
        third_value_all += list_third
    third_value_all = round(third_value_all / len(third_value),2)
    return third_value_all


# aa.write(+'\n')
# aa.close()