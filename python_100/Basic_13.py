## class 

# # 1 
# # 사람 (Human) 클래스에 "응애응애"를 출력하는 생성자를 추가
# class Hm:
#     def __init__(self):
#         print("응애응애")
        
# areum = Hm()

# # 2 
# class Hm:
#     def __init__(self, name, age, sex):
#         self.name = name 
#         self.age = age
#         self.sex = sex

# areum = Hm("아름", 25, "여자")
 
# print(areum.name)

# # 3
# # 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 setInfo 메소드를 추가
# class Hm:
#     def __init__(self, name, age, sex):
#         self.name = name 
#         self.age = age
#         self.sex = sex
        
#     def who(self):
#         print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.sex))
        
        
#     def senInfo(self, name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
        
        
#     def __del__(self):
#         print("나의 죽음을 알리지 말라")
        

# areum = Hm("불명", "미상", "모름")
# areum.who()
# areum.senInfo("아름", "25", "여")
# areum.who()
# del(areum)

# # 4 
# # 주식 종목에 대한 정보를 저장하는 stock class 생성
# # 종목명과 종목코드를 입력받을 수 잇는 생성자 정의 
# # 객체에 종목코드를 입력할 수 있는 set_code 메서드 추가 
# # 종목명과 종목코드를 리턴하는 메서드 추가 
# # per, pbr, 배당 수익률 입력 받을 생성자 수정(float 타입)
# # PER, PBR, 배당수익률은 변경될 수 있는 값입니다. 이 값을 변경할 때 사용하는 set_per, set_pbr, set_dividend 메서드를 추가

# from typing import Any


# class stock:
#     def __init__(self, name, code, per, pbr, er):
#         self.name = name
#         self.code = code
#         self.per = per 
#         self.pbr = pbr
#         self.er = er 
        
        
#     def set_name(self, name):
#         self.name = name
#         print("이름: {} ".format(self.name))
        
#     def set_code(self,code):
#         self.code = code 
#         print("종목 코드: {} ".format(self.code))
        
#     def re_n(self):
#         return self.name 
    
#     def re_c(self):
#         return self.code
    
        
#     # def get_nc(self):
#     #     print("이름: {}, 종목 코드: {} ".format(self.name, self.code))
    
#     def set_per(self, per):
#         self.per = per 
        
#     def set_per(self, pbr):
#         self.pbr = pbr 
        
#     def set_per(self, er):
#         self.er = er 
        
# ss = stock("삼성전자", "005930")
# ss.get_nc()
# print(ss.re_n(), ss.re_c()) 

# 5 
import random

class account:
    
    ac_count = 0 
    
    def __init__(self, m_name, money):
        self.m_name = m_name
        self.money = money 
        self.bank = "SC 은행"
        n1 = random.randint(0,999)
        n2 = random.randint(0,99)
        n3 = random.randint(0,999999)
        
        # n1 = str(n1).zfill(3)
        # n2 = str(n2).zfill(2)
        # n3 = str(n3).zfill(6)
        n1 = str(n1)
        n2 = str(n2)
        n3 = str(n3)
        self.ac_num = n1 + '-' +n2+ '-'+n3
        account.ac_count += 1 
        
    def count_num(cls):
        print(cls.ac_count)
        
    def deposit(slef, amount):
        if amount >= 1:
            slef.money += amount
            
    def withdraw(self, amount):
        if self.money > amount:
            self.money -= amount
    
    def display_info(self, ):
        print("은행이름: {}, 예금주: {}, 계좌번호: {}, 잔고: {}".format(self.bank, self.m_name, self.ac_count, self.money))
        
    
        
# mn = account("김민수", "100")
p = account("파이썬", 10000)
p.display_info()



