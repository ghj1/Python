n = int(input())
a = [125, 15232, 97]

# 이런 식으로도 list의 원소에 접근한다. 
# for x in a:
#     print(x)

# def digit_sum(x):
#     sum = 0 
#     while x >0:
#         sum += x%10
#         x = x// 10
#         return sum 

# max = -2147000000    
# for x in a:
#     tot = digit_sum(x)
#     if tot>max:
#         max=tot 
#         res= x

# print(res)


# 다른 방법
def digit_sum(x):
    sum = 0 
    for i in str(x):
        sum += int(i)
    return sum 
    #     print(i, end= ' ')
    # print()

max = -2147000000    
for x in a:
    tot = digit_sum(x)
    if tot>max:
        max=tot 
        res= x

print(res)
 