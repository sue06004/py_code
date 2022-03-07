import sys
input = sys.stdin.readline

N=int(input())
li=list(map(int,input().split()))
M=int(input())
dp=[[-1 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(0,N-i):
        x=i+j
        if x-j<2:
            if li[j]==li[x]:
                dp[j][x]=1
            else:
                dp[j][x]=0
        else:
            if dp[j+1][x-1] == 1 and li[j]==li[x]:
                dp[j][x]=1
            else:
                dp[j][x]=0

for _ in range(M):
    S,E=map(int,input().split())
    print(dp[S-1][E-1])

#팰린드롬인지 확인하는 방법은 [start+1][end-1]이 팰린드롬이고
#첫값과 끝값이 같으면 팰린드롬이다.

