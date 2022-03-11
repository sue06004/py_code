import sys
from collections import deque
input =sys.stdin.readline

n=int(input())
dp=[10000]*(n+1)
dp[n]=0
queue=deque()
queue.append(n)
while queue:
    x = queue.popleft()
    if x==1:
        continue
    if x%3==0 and dp[x//3]>dp[x]+1:
        dp[x//3]=dp[x]+1
        queue.append(x//3)
    if x%2==0 and dp[x//2]>dp[x]+1:
        dp[x//2]=dp[x]+1
        queue.append(x//2)
    if  dp[x-1]>dp[x]+1:
        dp[x-1]=dp[x]+1
        queue.append(x-1)
print(dp[1])