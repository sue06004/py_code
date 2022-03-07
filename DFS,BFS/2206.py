import sys
from collections import deque
input = sys.stdin.readline

n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().strip())))

def bfs():
    queue=deque()
    queue.append([0,0,1])
    visited=[[[0,0] for _ in range(m)] for _ in range(n)]
    visited[0][0][1]=1
    while queue:
        x,y,w=queue.popleft()
        if (x,y)==(n-1,m-1):
            return visited[x][y][w]
        if x>0 and graph[x-1][y]==0 and visited[x-1][y][w]==0:
            queue.append([x-1,y,w])
            visited[x-1][y][w]=visited[x][y][w]+1
        elif x>0 and graph[x-1][y]==1 and w==1:
            queue.append([x-1,y,0])
            visited[x-1][y][0]=visited[x][y][w]+1
        if x<n-1 and graph[x+1][y]==0 and visited[x+1][y][w]==0:
            queue.append([x+1,y,w])
            visited[x+1][y][w]=visited[x][y][w]+1
        elif x<n-1 and graph[x+1][y]==1 and w==1:
            queue.append([x+1,y,0])
            visited[x+1][y][0]=visited[x][y][w]+1
        if y>0 and graph[x][y-1]==0 and visited[x][y-1][w]==0:
            queue.append([x,y-1,w])
            visited[x][y-1][w]=visited[x][y][w]+1
        elif y>0 and graph[x][y-1]==1 and w==1:
            queue.append([x,y-1,0])
            visited[x][y-1][0]=visited[x][y][w]+1
        if y<m-1 and graph[x][y+1]==0 and visited[x][y+1][w]==0:
            queue.append([x,y+1,w])
            visited[x][y+1][w]=visited[x][y][w]+1
        elif y<m-1 and graph[x][y+1]==1 and w==1:
            queue.append([x,y+1,0])
            visited[x][y+1][0]=visited[x][y][w]+1
    return -1
print(bfs())