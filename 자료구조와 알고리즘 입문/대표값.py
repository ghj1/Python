from posixpath import split
import sys 
sys.stdin = open("자료구조와 알고리즘 입문/input_대표값.txt", "r")
n = int(input())
a = list(map(int, input().split()))
ave = round(sum(a)/n) # 평균

min = 2147000000 # 정수형 크기의 가장 큰 값
for idx, x in enumerate(a):
    tmp = abs(x - ave) # abs는 절대값을 반환해주는 함수
    if tmp<min:
        min = tmp 
        score = x 
        res = idx+1 
        
    elif tmp == min :
        if x > score:
            score = x
            res = idx+1 
            
print(ave, res)
    
