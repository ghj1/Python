# 분기문 : program 중 true or false를 반환하는 
# 조건식 결과에 따라 프로그램을 어떤 경로로 실행할지 결정하는 문
# a = input("입력하세요: ")

# if a == "안녕하세요":
#     print(a,a)
# else:
#     print("다시 입력해주세요.")
    
# 다른 result
# print(a * 2)

# num_en = int(input("숫자를 입력하세요: "))

# print(num_en + 10)

# 짝수/홀수 판별 
# enter = int(input("숫자 입력: "))
# num_eo = enter%2

# if num_eo == 0:
#     print("짝수")
# else: 
#     num_eo == 1
#     print("홀수")
    
    
# Q2
# enter = int(input("숫자 입력: "))
# if enter > 255:
#     print(255)
# else: 
#     enter < 255
#     print(enter + 20)

# Q3
# enter = int(input("숫자 입력: "))

# if enter < 0:
#     print(0)

# elif enter > 255:
#     print(255)

# else:
#     print(enter-20)
    
# Q3

# enter = input("시간을 입력하세요: ")

# if enter[-2:] == "00":
#     print("정각 입니다.")
# else:
#     print("정각이 아닙니다.")
    

# Q4
# enter = input("좋아하는 과일은? ")
# fruit = ["사과", "포도", "홍시"]

# if enter in fruit :
#     print("정답입니다.")
# else: 
#     enter not in fruit
#     print("오답입니다.")

#Q5 
# enter = input("좋아하는 과일은? ")
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# ke = list(fruit.keys())
# va = list(fruit.values())

# if enter in ke:
#     print("정답입니다.")
# else:
#     enter in va
#     print("오답입니다.")

#Q6 
# enter = input("입력하세요: ")
# tf = enter.islower()

# if tf == True:
#     et = enter.upper()
#     print(et)
# else:
#     tf == False
#     ef = enter.lower()
#     print(ef)
    
    
#Q7 
# enter = int(input("점수를 입력하세요: "))

# if enter >= 81 and enter <= 100:
#     print("grafe is A")
# elif enter >= 61 and enter <= 80:
#     print("grafe is B")
# elif enter >= 41 and enter <= 60:
#     print("grafe is C")
# elif enter >= 21 and enter <= 40:
#     print("grafe is D")
# elif enter >= 0 and enter <= 20:
#     print("grafe is E")

#Q8
# enter = input("입력: ")

# a = list(enter.split(" ")) 
# num = int(a[0])
# div = a[1]

# if div == "달러":
#     print(num * 1167,"원")
# elif div == "엔":
#     print(round(num * 1.096, 3), "원")
# elif div == "유로":
#     print(num * 1268, "원")
# elif div == "위안":
#     print(num * 171, "원")

#Q9 
# num_ls = []
# num1 = num_ls.append(int(input("입력: ")))
# num2 = num_ls.append(int(input("입력: ")))
# num3 = num_ls.append(int(input("입력: ")))

# re = max(num_ls)
# print(re)

#Q10 
# enter = input("휴대전화 번호 입력: ")
# en_p = enter.split("-")

# if en_p[0] == "011":
#     print("당신은 SKT 사용자입니다.")
# elif en_p[0] =="016":
#     print("당신은 KT 사용자입니다.")
# elif en_p[0] =="019":
#     print("당신은 LGU 사용자입니다.")
# else:
#     print("통신사를 알 수 없습니다.")
    
#Q11
# enter = input("우편번호: ")
# zip_code = enter[2]

# if zip_code in ["0", "1", "2"]:
#     print("강북구")
# elif zip_code in ["3", "4", "5"]:
#     print("도봉구")
# else:
#     zip_code in ["6", "7", "8", "9"]
#     print("노원구")

#Q12
# enter = input("주민등록번호: ")
# num = enter[7]

# if num in ["1","3"]:
#     print("남자")
# else: 
#     num in ["2", "4"]
#     print("여자")
    
#Q13
# enter = input("주민등록번호: ")
# n = enter.split("-")
# n_1 = n[0]
# n_2 = n[1]
# b = 0
# ab = 0 
# bj = 0 
# for i in range(0,6):
#     a = int(n_1[i])
#     b = b+(a*(i+2))

# for r in range(0,2):
#     ar = int(n_2[r])
#     ab = ab+(ar*(i+8))

# for j in range(2,6):
#     aj = int(n_2[j])
#     bj = bj+(aj*(j))
    
# re = (b+ab+bj) % 11
# result = 11 - re

# if result == int(n_2[6]):
#     print("유효한 주민등록번호 입니다.")
# else: 
#     print("유효하지 않은 주민등록번호 입니다.")

#Q14

import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
# btc 딕셔너리 안에는 시가, 종가, 최고가, 최저가 등이 저장되어 있다. 
# 최고가와 최저가의 차이를 변동폭으로 정의할 때 (시가 + 변동폭)이 최고가 보다 
# 높을 경우 "상승장", 그렇지 않은 경우 "하락장" 문자열을 출력하라.

print(btc)

