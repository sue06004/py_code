
#검색으로 품
import sys
input = sys.stdin.readline

n=int(input())
a=list(map(int,input().split()))

dp=[[0]*n for _ in range(2)]
dp[0][0]=a[0]

if n>1:
    result=-sys.maxsize
    for i in range(1,n):
        dp[0][i]=max(dp[0][i-1]+a[i],a[i])
        dp[1][i]=max(dp[1][i-1]+a[i],dp[0][i-1])
        result=max(result,dp[0][i],dp[1][i])
    print(dp)
    print(result)
else:
    print(dp[0][0])