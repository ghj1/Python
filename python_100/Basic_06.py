#list 생성
ls = ["doctor", "split", "lucky"]
print(ls)

# 생성된 list에 추가 
ls.append ("Batman")
print(ls)

# 특정 index에 원소 추가
ls.insert(1, "superman")

print(ls)

# 특정 index 원소 삭제 "Batman" 삭제
# del 을 사용하면 list 원소가 삭제되고 남은 값들이 새로 indexing 되어서 
# 여러 값을 삭제할 떄는 어떤 값을 먼저 삭제하고 새로 매겨진 index값을 고려해 삭제해야 한다. 
del ls[4]
print(ls)

# 두개의 list를 하나로 만들기
ls1 = ["a", "b", "c" ] 
ls2 = ["d", "e", "f"]
als = ls1+ls2
print(als)

#list에서 최대값, 최솟값 출력 
ls_m = [1,2,3,4]
ls_max = max(ls_m)
ls_min = min(ls_m)
print(ls_max)
print(ls_min)

# list 합 출력 
ls_sum = sum(ls_m)
print(ls_sum)
# print(sum(ls_m))

# list len
cook = ["피자", "김밥", "만두", "양념치킨", 
        "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]

print(len(cook))

# list 평균
average = sum(ls_m) /len(ls_m)
print(average)

# 슬라이싱 
price = ['20180728', 100, 130, 140, 150, 160, 170]

print(price[1:])
print(price[::2])

nums = [1,2,3,4,5,6,7,8,9,10]

print(nums[1::2])

print(nums[::-1])

# join method 
# list에 있는 요소들을 다 합쳐서 문자열 
