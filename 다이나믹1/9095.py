import sys
input = sys.stdin.readline

T=int(input())
dp=[0]*11
dp[1]=1
dp[2]=2
dp[3]=4
start=4
for _ in range(T):
    n=int(input())
    if dp[n]!=0:
        print(dp[n])
        continue
    for i in range(start,n+1):
        dp[i]=dp[i-3]+dp[i-2]+dp[i-1]
    start=n+1
    print(dp[n])