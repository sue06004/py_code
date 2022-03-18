import sys
input = sys.stdin.readline
# 최적화풀이

n=int(input())
a=list(map(int,input().split()))

dp=[0]*n #합
dp[0]=a[0]
mx=a[0]
for i in range(1,n):
    for j in range(i):
        if a[j]<a[i] and dp[j]>dp[i]:
            dp[i]=dp[j]
    dp[i]+=a[i]
    mx = max(mx,dp[i])

print(mx)