import sys
from collections import deque
input=sys.stdin.readline

def bfs():
    queue=deque()
    queue.append(a)
    graph=[[0,-1] for _ in range(100001)]
    graph[a]=[1,0]
    while queue:
        x=queue.popleft()
        if 0<=x+1<100001:
            if graph[x+1][0]==0 and not graph[b][0]:
                queue.append(x+1)
                graph[x+1][1]=graph[x][1]+1
            if graph[x+1][1]==graph[x][1]+1:
                graph[x+1][0]+=graph[x][0]
        if 0<=x-1:
            if graph[x-1][0]==0 and not graph[b][0]:
                queue.append(x-1)
                graph[x-1][1]=graph[x][1]+1
            if graph[x-1][1]==graph[x][1]+1:
                graph[x-1][0]+=graph[x][0]
        if x*2<100001:
            if graph[2*x][0]==0 and not graph[b][0]:
                queue.append(2*x)
                graph[2*x][1]=graph[x][1]+1
            if graph[2*x][1]==graph[x][1]+1:
                graph[2*x][0]+=graph[x][0]
    print(graph[b][1])
    print(graph[b][0])

a,b=map(int,input().split())
bfs()