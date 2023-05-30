import sys 
sys.stdin = open("/Users/gimhyeonjeong/Desktop/python/자료구조와 알고리즘 입문/input.txt", "r")
n,k = map(int, input().split())
cnt=0 
for i in range(1, n+1):
    if n%i==0:
        cnt+=1 
    if cnt==k:
        print(i) 
        break 
else:
    print(-1)