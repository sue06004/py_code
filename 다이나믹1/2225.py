import sys
input = sys.stdin.readline

n,k=map(int,input().split())

dp=[[0]*k for _ in range(n+1)]
dp[1]=[1]*k
for i in range(2,n+1):
    prev=sum(dp[i-1])
    li=[0]*k
    for j in range(k):
        if j==0:
            li[j]=prev
        else:
            li[j]=li[j-1]-dp[i-1][j-1]
    dp[i]=li

print(sum(dp[n])%1000000000)