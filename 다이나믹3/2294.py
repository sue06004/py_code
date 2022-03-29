import sys
input = sys.stdin.readline

n,k=map(int,input().split())
dp=[1000000]*(k+1)
dp[0]=0
li=[]
for _ in range(n):
    c=int(input())
    if c in li:
        continue
    li.append(c)
    for i in range(c,k+1):
        dp[i]=min(dp[i],dp[i-c]+1)

if dp[k]==1000000:
    print(-1)
else:
    print(dp[k])
