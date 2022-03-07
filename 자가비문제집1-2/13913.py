import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue=deque()
    queue.append((a,0))
    graph[a]=a
    while queue:
        x,y=queue.popleft()
        if x==b:
            i=b
            while i!=a:
                result.append(i)
                i=graph[i]
            result.append(a)
            return y
        if 0<=x+1<100001 and graph[x+1]==-1:
            queue.append((x+1,y+1))
            graph[x+1]=x
        if 0<=x-1<100001 and graph[x-1]==-1:
            queue.append((x-1,y+1))
            graph[x-1]=x
        if 0<=x*2<100001 and graph[x*2]==-1:
            queue.append((x*2,y+1))
            graph[x*2]=x

a,b=map(int,input().split())
graph=[-1 for _ in range(100001)]
result=[]
print(bfs())
print(" ".join(map(str,result[::-1])))