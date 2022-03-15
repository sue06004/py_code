import sys
import math
input =sys.stdin.readline

n=int(input())

dp=[x for x in range(n+1)]
for i in range(1,n+1):
    a = int(math.sqrt(i))
    if a**2==i:
        dp[i]=1
        continue
    for j in range(1,a+1):
        dp[i]=min(dp[i],dp[i-(j**2)]+dp[j**2])
print(dp[n])