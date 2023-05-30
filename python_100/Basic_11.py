#함수 def

# 1 
# 하나의 문자를 입력받아 문자열 끝에 ":D" 스마일 문자열을 이어 붙여 출력하는 print_with_smile 함수를 정의하라.

def print_with_smile(string):
    print(string+":D")
    
print_with_smile("안녕")


# 2 
# 현재 가격을 입력 받아 상한가 (30%)를 출력하는 print_upper_price 함수를 정의하라.
def upp_price(int):
    print(int*1.3)

upp_price(40)

# 3
# 두 개의 숫자를 입력받아 두 수의 합을 출력하는 print_sum 함수를 정의하라.
def print_sum(a,b):
    print(a+b)
    
# 4 
# 두 개의 숫자를 입력받아 합/차/곱/나눗셈을 출력하는 함수 작성
def arith_oper(a,b):
    print(f"{a}+{b} = {a+b}")
    print(f"{a}-{b} = {a-b}")
    print(f"{a}*{b} = {a*b}")
    print(f"{a}/{b} = {round(a/b,2)}")
    
arith_oper(1,3)


# 5
# 세 개의 숫자를 입력받아 가장 큰수를 출력하는 함수를 정의(단 if문을 사용)
def p_max(a,b,c):
    re = 0 
    # if a > b and a > c:
    #     print(a)
    # elif b > a and b > c:
    #     print(b)
    # elif c > a and c > b:
    #     print(c)
    
    # antoehr result 
    if a > re:
        re = a 
    if b > re:
        re = b
    if c > re:
        re = c
    print(re)

p_max(4,9,7) 


# 6 
# 입력된 문자열을 역순으로 출력하는 함수를 정의하라.

def pri_rev(string):
    print(string[::-1])
    
pri_rev("python")


# 7
# 성적 리스트를 입력 받아 평균을 출력하는 함수 정의 

def pr_sc(list):
    print(sum(list)/len(list))

pr_sc([1,2,3])

# 8 
# 하나의 리스트를 입력받아 짝수만 화면에 출력하는 함수를 정의하라.

def pr_ev(list):
    for i in list:
        if i % 2 == 0:
            print(i)

pr_ev([1, 3, 2, 10, 12, 11, 15])


# 9
# 하나의 딕셔너리를 입력받아 딕셔너리의 key 값을 화면에 출력하는 함수를 정의하라.
def pr_key(dict):
    for i in dict.keys():
        print(i)

pr_key({"이름":"김말똥", "나이":30, "성별":0})

# 10 
# my_dict와 날짜 키값을 입력받아 OHLC 리스트를 출력하는 함수를 정의

my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}

def pri_valbykey(my_dict, key):
    print(my_dict[key])
    
pri_valbykey(my_dict, "10/27")

# 11
# 입력 문자열을 한 줄에 다섯글자씩 출력하는 함수를 작성하라.
def p_5s(string):
    # print(string[0:5])
    # print(string[5:])
    
# another result
    sn = int(len(string)/5)
    for i in range(sn+1):
        print(string[i*5:i*5+5])
        

p_5s("아이엠어보이유알어걸")

# 12
# 문자열과 한줄에 출력될 글자 수를 입력을 받아 한 줄에 입력된 글자 수만큼 출력하는 함수를 작성하라.
def p_s(string, a):
    sn = int(len(string)/a)
    for i in range(sn+1):
        print(string[i*a:i*a+a])

p_s("아이엠어보이유알어걸", 3)



# 13 
# 연봉을 입력받아 월급을 계산하는 함수를 정의
# 회사는 연봉을 12개월로 나누어 분할 지급하며, 이 때 1원 미만은 버림한다.

def money(ap):
    mp = int(ap/12)
    return print(mp)

money(12000000)

# 14
# 문자열 하나를 입력받아 인터넷 주소를 반환하는 함수를 정의
def make_url(string):
    print(f"www.{string}.com")

make_url("naver")


# 15 
# 문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는 함수를 정의

def mk_li(string):
    return print(list(string))

mk_li('abcd')


# 16 
# 숫자로 구성된 하나의 리스트를 입력받아, 짝수들을 추출하여 리스트로 반환하는 pickup_even 함수 구현 

def mk_even(list):
    re = []
    for i in list:
        if i % 2 == 0:
            re.append(i)
    return print(re)

mk_even([3, 4, 5, 6, 7, 8])

# 17 
# 콤마가 포함된 문자열 숫자를 입력받아 정수로 변환하는 함수를 정의하라.

def con_int(str):
    a = str.replace(',', '')
    re = int(a)
    return print(re) 

con_int("1,234,567")



    

            