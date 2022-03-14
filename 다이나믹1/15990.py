import sys
input = sys.stdin.readline

T=int(input())
dp=[[],[1,0,0],[0,1,0],[1,1,1]]
last=4
for _ in range(T):
    n=int(input())
    if len(dp)-1>=n:
        print(sum(dp[n])%1000000009)
        continue
    for i in range(last,n+1):
        tmp=[0,0,0]
        tmp[0]=(dp[i-1][1]+dp[i-1][2])%1000000009
        tmp[1]=(dp[i-2][0]+dp[i-2][2])%1000000009
        tmp[2]=(dp[i-3][0]+dp[i-3][1])%1000000009
        dp.append(tmp)
    last=n+1
    print(sum(dp[n])%1000000009)

