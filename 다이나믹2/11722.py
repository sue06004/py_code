import sys
input = sys.stdin.readline

n=int(input())
a=list(map(int,input().split()))
dp=[0]*n
for i in range(n):
    for j in range(i):
        if a[j]>a[i]:
            dp[i]=max(dp[i],dp[j])
    dp[i]+=1

print(max(dp))