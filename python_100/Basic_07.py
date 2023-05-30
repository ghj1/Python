# Tuple? 값이 변하지 않는 것이 특징, 요소 삭제, 변경이 불가, 중복된 값을 넣을 수 있음
# 튜플 만들기
at = ()

print(type(at))

movie= ('소울', '범죄도시', '굿윌헌팅')

# tuple을 list로 변화 
ttl = list(movie)
print(ttl)

# uppacking 변수의 데이터를 각각의 변수로 변환하는 method
list_n = (1,2,3)
a,b,c = list_n
print(a,b,c)

# *를 붙이면 나머지 값들을 list 형태로 가지고 옴
a, *b, c = [1,2,3,4,5,6]
print(a)
print(*b)
print(c)

d, f, *g = [1,2,3,4,5,6]
print(d)
print(f)
print(*g)

# values()  : 값만 , items() : 키와 값 모두 가져온다. 
a, b, c = {'k1':1, 'k2':2, 'k3':3}.values()
print(a,b,c)

a, b, c = {'k1':1, 'k2':2, 'k3':3}.items()
print(a,b,c)

# **를 붙이면 dict의 key와 value 값 모두 가져올 수 있다. 

d1 = {'k1': 1}
d2 = {'k2': 2, 'kk2': 3}
d3 = {'k3': 4, 'kk3': 5}

d = {**d1}
print(d)

# range 함수 

da = tuple(range(2,100,2))
print(da)

dl = list(range(1,100,3))
print(dl)

