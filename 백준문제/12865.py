import sys
input = sys.stdin.readline

n,k=map(int,input().split())
li=[[0,0]]
for _ in range(n):
    li.append(list(map(int,input().split())))

dp=[[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,k+1):
        w=li[i][0]
        v=li[i][1]
        if j >= w:
            dp[i][j]=max(v+dp[i-1][j-w],dp[i-1][j])
        else:
            dp[i][j]=dp[i-1][j]


print(dp[-1][-1])