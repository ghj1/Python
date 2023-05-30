arr = [5, 3, 7, 9, 2, 5, 2, 6]
arrMin= float('inf')
for i in range(len(arr)):
    if arr[i]<arrMin:
        arrMin = arr[i]
        
print(arrMin)
 

# 다른 방법
arr = [5, 3, 7, 9, 2, 5, 2, 6]
arrMin= arr[0] # 무한대 값으로 안하고 첫번째 값으로 해도 됨
for i in range(len(arr)):
    if arr[i]<arrMin:
        arrMin = arr[i]        
print(arrMin)

# 다른 방법 2
arr = [5, 3, 7, 9, 2, 5, 2, 6]
arrMin= float('inf')
for  x in arr:
    if x < arrMin:
        arrMin = x
        
print(arrMin)
