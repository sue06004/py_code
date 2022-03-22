import sys
from collections import deque
input = sys.stdin.readline

n,m=map(int,input().split())
maze=[list(map(int,input().split())) for _ in range(n)]

dp=[[0]*m for _ in range(n)]
dp[0][0]=maze[0][0]
for i in range(n):
    if i!=0:
        dp[i][0]=dp[i-1][0]+maze[i][0]
    for j in range(1,m):
        if i==0:
            dp[i][j]=dp[i][j-1]+maze[i][j]
        else:
            dp[i][j]=max(dp[i][j-1]+maze[i][j],dp[i-1][j]+maze[i][j])

print(dp[n-1][m-1])