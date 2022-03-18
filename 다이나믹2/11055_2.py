import sys
input = sys.stdin.readline
# 첫 시도풀이, 이상함
n=int(input())
a=list(map(int,input().split()))

dp=[[] for _ in range(n)]

for i in range(n):
    for j in range(i):
        if sum(dp[i])<sum(dp[j]) and dp[j][-1]<a[i]:
            dp[i]=dp[j][:]
    dp[i]+=[a[i]]
mx=0
for i in range(n):
    mx = max(mx,sum(dp[i]))
print(mx)