def add(a,b):
    c = a+b
    print(c)
    
add(3,2)

def add(a,b):
    c = a+b 
    return c   #결과값을 반환 

    
print(add(3,2))


def add(a,b):
    c = a+b
    d = a-b
    return c, d

print(add(3,2)) # tuple 자료구조 형태로 여러값을 출력


# x가 소수이면 참을 출력하고 소수가 아니면 거짓을 출력
def isPrime(x):
    for i in range(2, x):
        if x%i == 0:
            return False
        
    return True 

a = [12, 13, 7, 9, 19]
for x in a:
    if isPrime(x):
        print(x, end = ' ')
        