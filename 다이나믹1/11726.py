import sys
input = sys.stdin.readline

n=int(input())
dp=[0]*1001
dp[1]=1
dp[2]=2
for i in range(3,n+1):
    dp[i]=(dp[i-2]+dp[i-1])%10007

print(dp[n])

#dp[i]는 dp[i-2]에서 끝에 가로줄 1*2모양의 직사각형2개를 놓는 경우와
#dp[i-1]의 끝에 세로줄 2*1모양의 직사각형 1개를 놓는 경우의 합이다.