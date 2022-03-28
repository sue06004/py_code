import sys
input = sys.stdin.readline

n,k=map(int,input().split())
dp=[0]*(k+1)

for _ in range(n):  
    c=int(input())
    if c<=k:
        dp[c]+=1
    for i in range(c+1,k+1):
        dp[i]+=dp[i-c]
print(dp[k])
