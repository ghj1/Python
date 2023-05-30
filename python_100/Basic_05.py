# #1 print 기초 
# print("Hello Wrold")

# #2 Print 기초 
# print("Mary's cosmetics")
# #3
# print('신씨가 소리 질렀다. "도둑이야".')
# #4 
# print("C:\Windows")
# #5 ('\t' 는 탭을 의미 | '\n'은 줄바꿈 의미)
# print("안녕하세요.\n만나서\t\t반갑습니다.")

# #6 
# print("오늘은", "일요일")
# print("nver;kakao;sk;samsung")
# print("nver/kakao/sk/samsung")

# # 다른 방법
# print("naver", "kakao", "samsung", sep=";")
# print("naver", "kakao", "samsung", sep="/")
# print("first") ; print("second")
# #(세미콜론은 한 줄에 여러개 명령을 작성하기 위해 사용하며 줄바꿈 없이 출력하려면 "end =" 함수 이용)
# print("first", end="");print("second")


#11~20 연습 
# sm = 50000
# enter = int(input("몇 주를 보유하고 있는지 입력하세요: "))
# result = sm*enter

# print(result)

# 시가총액 = 298000000000
# 현재가 = 50000
# PER = 15.79
# print(시가총액, type(시가총액))
# print(현재가, type(현재가))
# print(PER, type(PER))

# s = "helllo"
# t = "python"

# print(s+"!",t)

# lang = "python"

# print(lang[0], lang[2])

# license_plate = "24가 2210"

# print(license_plate[-4: ])

# string = "홀짝홀짝홀짝"

# a[start:end:step][시작:끝:단계]
# print(string[::2])

# print(string[::-1])

# #replace 함수 replace(old, new, [count])

# phone_number = "010-1111-2222"
# phone_number1 = phone_number.replace("-", " ")

# print(phone_number1)

# url = "http://sharebook.kr"
# url_p = url.split(".")

# print(url_p[-1])

# 문자열 출력
# n1 = "이수" 
# age1 = 23
# n2 = "도진"
# age2 = 30

# print("이름: %s 나이: %d" % (n1, age1))
# print("이름: %s 나이: %d" % (n2, age2))

# print("이름: {} 나이: {}".format(n1, age1))
# print("이름: {} 나이: {}".format(n2, age2))

# print(f"이름: {n1} 나이: {age1}")
# print(f"이름: {n2} 나이: {age2}")

# 특정 문자 출력

# text = "5,969,782,550"
# te1 = int(text.replace(",", ""))

# print(te1)

# # 문자열에서 '2020/03'만 출력
# 분기 = "2020/03(E) (IFRS연결)"

# print(분기[0:7])

# # strip method
# data = "   삼성전자    "
# da1= data.strip()

# print(da1)

# upper method
cd = "krw"
cu = cd.upper()
cdd = cu.lower()
print(cu)
print(cdd)

# capitalize() -> 문자열의 첫글자는 대문자로, 나머지는 소문자로 변환하는 메소드
con_cap = "hello"
con_cap2 = "HELLO"
a = con_cap.capitalize()
b = con_cap2.capitalize()
print(a); print(b)

# endswith method -> 특정한 문자열로 끝나는지 여부를 T/F 형식으로 반환하는 메소드
name = "report.xlsx"
re = name.endswith("xlsx")
print(re)

#startswith method -> 특정한 문자열로 시작하는지 여부를 T/F 형식으로 반환하는 메소드 
res = name.startswith("report")
print(res)

#split method -> 특정 기준으로 문자열을 구분해 나눠 list로 만들어주는 메소드 
# rsplit은 오른쪽에 특정 기준을 lsplit은 왼쪽에 특정 기준을 구분
name_s = "hello world"
name_as = "hello, Jin"
name_sp = name_s.split(" ")
name_asp = name_as.split(",")
print(name_sp)
print(name_asp) 