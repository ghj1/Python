# pyhton for문 and range , 반복문
#1 
# ls = ['dog', 'cat', 'parrot']

# for i in range(0,3):
#     a = ls[i][0]
#     print(a)
    
#2 
# ls = [1,2,3]

# for i in range(0,3):
#     print(f"3 x {ls[i]}")
    
#3 
# ls = [1,2,3]

# for i in range(0,3):
#     print(f"3 x {ls[i]} = {3*ls[i]}" )
    
#4 나, 라만 출력
# ls = ["가", "나", "다", "라"]
# for i in range(0,4,2):
#     print(ls[i])

#5 20보다 작은 3의 배수 출력 
# ls = [13, 21, 12, 14, 30, 18]

# for i in ls:
#     if (i % 3) == 0 and (i < 20):
#         print(i)

#6 3글자 이상 문자만 출력 
# ls = ["I", "study", "python", "language", "!"]

# for i in ls:
#     if len(i) >= 3:
#         print(i)

#7 대문자만 출력
# ls = ["A", "b", "c", "D"]

# for i in ls:
#     if i.isupper() == True:
#         print(i)
        
        
#8 첫문자만 대문자로 변환
# ls = ['dog', 'cat', 'parrot']

# # 8_1re
# for i in ls:
#     print(i.capitalize())

# # 8_2re
# for j in ls:
#     aj = j[0]
#     au = aj.upper()
#     print(au + j[1:])


# 9  확장자 제거 하고 출력
# ls = ['hello.py', 'ex01.py', 'intro.hwp']   

# for i in ls:
#     a = i.split('.')
#     b = a[0]
#     print(b)
    
# 10 확장자가 .h인 파일만 출력 
# ls = ['intra.h', 'intra.c', 'define.h', 'run.py']
# for i in ls:
#     a = i.split('.')
#     b = a[0]
    
#     if a[1] == 'h':
#         print(i)
        
# 11 확장자가 .h나 .c인 파일만 출력
# ls = ['intra.h', 'intra.c', 'define.h', 'run.py']
# for i in ls:
#     a = i.split('.')
#     b = a[0]
    
#     if a[1] == 'h' or a[1] == 'c':
#         print(i)
        
        
# 12 1~10까지 모두 더한 값을 출력하는 프로그램
# sm = 0 
# for i in range(1,11):
#     sm += i # sm = sm + i
# print(f"합: {sm}")

# # 12 1~10 중 홀수의 합 출력
# sm = 0 
# for i in range(1,11):
#     if i % 2== 1:
#         sm += i 
# print(f"합: {sm}")

# 13 1~10숫자를 모두 곱한 값 출력 
# sm = 1
# for i in range(1,11):
#     sm *= i
# print(sm)

# 14
# 반복문과 range를 사용해 아래와 같이 출력 
# 라 다
# 다 나
# 나 가

# ls = ["가", "나", "다", "라"]

# for i in range(len(ls)-1,0,-1):
#     print(ls[i], ls[i-1])
    
# 15 
# ls = [100, 200, 400, 800]

# for i in range(len(ls)-1):
#     m = ls[i+1] -ls[i]
#     print(m)
    
# 16 
# ls = [100, 200, 400, 800, 1000, 1300]

# for i in range(1,len(ls)-1):
#     a = (ls[i-1]+ls[i]+ls[i+1])/3
#     print(a)

# # 17 
# lr = [100, 200, 400, 800, 1000]
# hp = [150, 300, 430, 880, 1000]

# li = []

# for i in range(len(lr)):
#     li.append(hp[i] - lr[i])
# print(li)

# 18
# li = [[101,102],[201,202],[301,302]]
# print(li)

# 19
# stock ={"시가":[100,200,300], "종가":[80,210,330]}

# 20
# apart = [ [101, 102], [201, 202], [301, 302] ]

# for i in range(3):
#     for j in range(2):
#         print(apart[i][j],"호")

# another result
# for i in apart:
#     for j in i:
#         print(j,"호")
        

# 21 : 301호 302호 ~ 102호 순으로 출력
# apart = [ [101, 102], [201, 202], [301, 302] ]

# # for i in range(3,0,-1):
# #     for j in range(2):
# #         print(apart[i-1][j],"호")

# # anotehr result
# for i in apart[::-1]:
#     for j in i:
#         print(j, "호")

# # 22: 302호 301호 202호 201호 102호 101호 순으로 출력 
# for i in apart[::-1]:
#     for j in i[::-1]:
#         print(j,"호")

# 23 101호 ----- 출력
# apart = [ [101, 102], [201, 202], [301, 302] ]

# for i in apart:
#     for j in i:
#         print(j,"호\n","-"*5)  
        
# # 24 101호 102호 ----- 출력         
# for i in apart:
#     for j in i:
#         print(j, "호")
#     print("-----")
    

# # 25
# for i in apart:
#     for j in i:
#         print(j, "호")
# print("-----")

# # 26
# data = [
#     [ 2000,  3050,  2050,  1980],
#     [ 7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]

# result = []

# for i in data:
#     a = []
#     for j in i:
#         a.append(j*1.00014)
#     result.append(a)
# print(result)



# 27 100,190,310만 출력
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]

# for i in ohlc[1:]:
#     for j in i[3:]:
#         print(j)

# another result 
# for i in ohlc[1:]:
#     print(i[3])


# 28  
# ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장돼 있다. 
# 종가가 150원보다 큰경우에만 종가를 출력하라.

ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]


# for i in ohlc[1:]:
#     if i[3] > 150:
#         print(i[3])
        
# 29 
# 종가가 시가 보다 크거나 같은 경우에만 종가를 출력하라.

# for i in ohlc[1:]:
#     if i[3] >= i[0]:
#         print(i[3])

# 30 
# 고가와 저가의 차이를 변동폭으로 정의할 때 변동폭을 volatility 이름의 리스트에 저장하라.

# volatility = []

# for i in ohlc[1:]:
#     volatility.append(i[1]-i[2])
# print(volatility)

# 31
# 종가가 시가보다 높은 날의 변동성 (고가 - 저가)을 화면에 출력하라.

for i in ohlc[1:]:
    if i[3] > i[0]:
        print(i[1]-i[2])
        
# 32
# 시가에 매수해서 종가에 매도 했을 경우 총 수익금을 계산하라.

a = 0 
for i in ohlc[1:]:
    a += (i[0]-i[3])
    
print(a)