import sys
from collections import deque
input = sys.stdin.readline


dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(gr):
    global n,m
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
                gr[ny][nx]=gr[y][x]+1
                queue.append((nx,ny))
            if nx==m-1 and ny==n-1:
                return


n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().strip())))

bfs(graph)
print(graph[n-1][m-1])