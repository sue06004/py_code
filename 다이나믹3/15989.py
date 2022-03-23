import sys
input = sys.stdin.readline

T=int(input())
dp=[[0,0,0] for _ in range(10001)]
dp[1]=[1,0,0]
dp[2]=[1,1,0]
dp[3]=[1,1,1]
last=4
for _ in range(T):
    n=int(input())
    for i in range(4,n+1):
        dp[i]=[dp[i-1][0],dp[i-2][0]+dp[i-2][1],dp[i-3][0]+dp[i-3][1]+dp[i-3][2]]
    
    print(sum(dp[n]))
    last=n+1
