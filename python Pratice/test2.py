# 단어 반복하기 

def re(s, n):
    sl = len(s)
    s_len = sl * n 
    st = s * s_len 
    return st[:n]  
    
st = input("단어를 입력하세요: ")
while True:
    
    number = int(input("숫자를 입력하세요: "))
    
    if (number < 0 or number > 10000):
        print("number은 10,000이하인 자연수 입니다. 다시 입력해주세요.")
    else: 
        break


result = re(st, number)
print(result)