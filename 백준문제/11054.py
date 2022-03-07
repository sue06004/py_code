n = int(input())
li = list(map(int,input().split()))

dp = [1 for _ in range(n)]
dp2 = [1 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if li[i] > li[j]:
            dp[i] = max(dp[i],dp[j]+1)
li_r=li[::-1]
for i in range(n):
    for j in range(i):
        if li_r[i] > li_r[j]:
            dp2[i] = max(dp2[i],dp2[j]+1)
dp2=dp2[::-1]

for i in range(n):
    dp[i]=dp[i]+dp2[i]

print(max(dp)-1)