import sys
input = sys.stdin.readline

T=int(input())
dp=[1,1,2,4]
last=4
for _ in range(T):
    n=int(input())
    if n<last:
        print(dp[n])
        continue
    for i in range(last,n+1):
        dp.append((dp[i-3]+dp[i-2]+dp[i-1])%1000000009)
    last=n+1
    print(dp[n])