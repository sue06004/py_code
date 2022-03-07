import sys
from collections import deque
input = sys.stdin.readline

dx=[0,0,-1,1]
dy=[-1,1,0,0]

def bfs(a,b):
    queue=deque()
    queue.append((a,b))
    distance=-1
    visit=[[False]*w for _ in range(h)]
    visit[a][b]=True
    while queue:
        distance+=1
        for _ in range(len(queue)):
            y,x=queue.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<w and 0<=ny<h and not visit[ny][nx] and graph[ny][nx]=="L":
                    queue.append((ny,nx))
                    visit[ny][nx]=True
    return distance
h,w=map(int,input().split())
graph=[list(input().strip()) for _ in range(h)]
result=0
for i in range(h):
    for j in range(w):
        if graph[i][j]=="L":
            result=max(result,bfs(i,j))
print(result)