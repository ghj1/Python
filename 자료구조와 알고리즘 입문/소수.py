n = int(input())

ch = [0]*(n+1)
cnt = 0 #소수의 갯수 
for i in range(2, n+1):
    if ch[i]==0:
        cnt+=1
        for j in range(1, n+1, i): # 소수의 배수들을 다 걸러냄
            ch[j]=1
            
print(cnt)

