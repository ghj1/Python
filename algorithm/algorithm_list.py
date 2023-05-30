# import random as r 
# a = [1,2,3,4,5,4]

# a.remove(4)
# print(a)

a= [23, 12, 36, 53, 19]

for i in range(len(a)):
    print(a[i], end= ' ')
print()

for x in a:
    print(x, end = ' ')
print()

# 위의 두가지는 같은 결과 값을 출력한다. 

for x in enumerate(a):
    print(x)
    

for x in enumerate(a):
    print(x[0], x[1])
print()
    
for index, value in enumerate(a):
    print(index, value)
print()

if all(60 >x for x in a):
    print("YES")
else:
    print("NO")
    
if any(15 >x for x in a):
    print("YES")
else:
    print("NO")