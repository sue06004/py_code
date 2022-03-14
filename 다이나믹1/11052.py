import sys
input = sys.stdin.readline

n=int(input())
p=list(map(int,input().split()))

dp=[0]*(n+1)

for i in range(1,n+1):
    dp[i]=p[i-1]
    for j in range(i):
        if dp[j]+dp[i-j]>dp[i]:
            dp[i]=dp[j]+dp[i-j]
print(dp[n])