import sys
input = sys.stdin.readline

n=int(input())
maze=list(map(int,input().split()))

dp=[1001]*n
dp[n-1]=0
for i in range(n-2,-1,-1):
    if maze[i]==0:
        dp[i]=-1
        continue
    for j in range(1,maze[i]+1):
        if i+j>=n:
            break
        if dp[i+j]<dp[i] and dp[i+j]!=-1:
            dp[i]=dp[i+j]
    if dp[i]==1001:
        dp[i]=-1
    else:
        dp[i]+=1

print(dp[0])