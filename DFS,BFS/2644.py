import sys
from collections import deque
input = sys.stdin.readline


def bfs(a,b,n,graph):
    queue=deque()
    queue.append(a)
    chon=0
    while queue:
        for _ in range(len(queue)):
            x=queue.popleft()
            if x==b:
                return chon
            for i in range(1,n+1):
                if graph[x][i]==1:
                    graph[x][i]=0
                    graph[i][x]=0
                    queue.append(i)
        chon+=1
    return -1
            
def sol():
    n=int(input())
    a,b=map(int,input().split())
    m=int(input())
    graph=[[0]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        x,y = map(int,input().split())
        graph[x][y]=1
        graph[y][x]=1
    print(bfs(a,b,n,graph))

            
sol()
