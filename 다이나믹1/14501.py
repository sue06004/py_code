import sys
input = sys.stdin.readline

n=int(input())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

dp=[0]*(n+1)
for i in range(n-1,-1,-1):
    if graph[i][0]+i==n:
        dp[i]=graph[i][1]
    elif graph[i][0]+i<n:
        dp[i]=max(dp[graph[i][0]+i:])+graph[i][1]

print(max(dp))