import sys
from collections import deque
input = sys.stdin.readline

dx=[0,0,-1,1]
dy=[-1,1,0,0]

def bfs():
    queue=deque()
    queue.append((0,0))
    visited=[[False]*n for _ in range(m)]
    visited[0][0]=True
    cnt=0
    while queue:
        y,x=queue.pop()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=ny<m and 0<=nx<n and not visited[ny][nx]:
                visited[ny][nx]=True
                if graph[ny][nx]==1:
                    graph[ny][nx]=0
                    cnt+=1
                else:
                    queue.append((ny,nx))
    return cnt
m,n=map(int,input().split())
graph=[]
for i in range(m):
    graph.append(list(map(int,input().split())))

def sol():
    li=[]
    cnt_=0
    while True:
        a=bfs()
        cnt_+=1
        li.append(a)
        if a==0:
            print(cnt_-1)
            print(li[-2])
            break
sol()
    




