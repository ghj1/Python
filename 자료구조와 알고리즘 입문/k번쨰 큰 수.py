import sys  
sys.stdin= open("/Users/gimhyeonjeong/Desktop/python/자료구조와 알고리즘 입문/input.txt", "rt")


n, k = map(int, input().split())
a = list(map(int, input().split()))
res=set() # 중복된 자료를 제거하는 것
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i]+a[j]+a[m])
res = list(res)  # set는 sort하는 기능이 없어서 list형태로 변환
res.sort(reverse=True)
print(res[k-1]) 