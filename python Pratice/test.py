# 하샤드수 점검 

while True:
    
    x = int(input("x값은? "))
    
    if (x < 1 or x > 10000):
        print('x는 1이상 10,000이하 숫자입니다. 다시 입력하세요.')
    else:
        break 

s = 0
for i in map(int, str(x)):
    s += i 
    
if x / s == 0:
    print(f"{x}의 모든 자릿수의 합은 {s}입니다. {x}은 {s}로 나누어 떨어지므로 {x}는 하샤드 수 입니다.")
elif not x / s == 0:
    print(f"{x}의 모든 자릿수의 합은 {s}입니다. {x}은 {s}로 나누어 떨어지지 않으므로 {x}는 하샤드 수가 아닙니다.")