import sys
input = sys.stdin.readline

n=int(input())
p=list(map(int,input().split()))

dp=[0]+p

for i in range(1,n+1):
    for j in range(i):
        dp[i]=min(dp[i],dp[j]+dp[i-j])
print(dp[n])