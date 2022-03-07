import sys
input = sys.stdin.readline

n,k=map(int,input().split())
coins=[]
cnt=0
for _ in range(n):
    coins.append(int(input()))
coins.sort()

dp=[0 for _ in range(k+1)]
dp[0]=1
for i in range(n):
    for j in range(1,k+1):
        if j-coins[i]>=0:
            dp[j]+=dp[j-coins[i]]
print(dp[k])

'''
dp[j]는 합이 j가 되는 경우의 수이다.
dp[0]=1로 초기화한다.
dp[j] = dp[j-coins[i]] + dp[j] 로 
j-coins[i]에다가 coins[j]를 더하면 j이므로
dp[j-coins[i]]를  dp[j]에 더하므로 dp[j]를 구할 수있다.
'''