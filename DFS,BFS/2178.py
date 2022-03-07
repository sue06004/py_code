import sys
from collections import deque
input = sys.stdin.readline

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(gr):
    global n,m
    gr[0][0]=0
    dp[0][0]=1
    queue=deque()
    queue.append((0,0))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=m or ny<0 or ny>=n:
                continue
            if gr[ny][nx]==1:
                gr[ny][nx]=0
                dp[ny][nx]=min(dp[ny][nx],dp[y][x]+1)
                queue.append((nx,ny))


n,m=map(int,input().split())
graph=[]
dp=[[n*m for _ in range(m)] for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int,input().strip())))

bfs(graph)
print(dp[n-1][m-1])
