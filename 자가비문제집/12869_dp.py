import sys
input = sys.stdin.readline

def sol(i,j,k):
    if i<0:
        return sol(0,j,k)
    if j<0:
        return sol(i,0,k)
    if k<0:
        return sol(i,j,0)
    if i==0 and j==0 and k==0:
        return 0
    result=dp[i][j][k]
    if result != -1:
        return result
    result=10000000
    if result>sol(i-9,j-3,k-1):
        result=sol(i-9,j-3,k-1)
    if result>sol(i-9,j-1,k-3):
        result=sol(i-9,j-1,k-3)
    if result>sol(i-3,j-9,k-1):
        result=sol(i-3,j-9,k-1)
    if result>sol(i-1,j-9,k-3):
        result=sol(i-1,j-9,k-3)
    if result>sol(i-1,j-3,k-9):
        result=sol(i-1,j-3,k-9)
    if result>sol(i-3,j-1,k-9):
        result=sol(i-3,j-1,k-9)
    result+=1
    dp[i][j][k]=result
    return dp[i][j][k]
n=int(input())
healths=list(map(int,input().split()))
while len(healths)<3:
    healths+=[0]
dp=[[[-1]*61 for _ in range(61)] for _ in range(61)]
print(sol(healths[0],healths[1],healths[2]))