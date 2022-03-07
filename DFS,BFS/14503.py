import sys
from collections import deque
input = sys.stdin.readline

def bfs(a):
    queue=deque()
    queue.append((r,c))
    cnt=1
    d=a
    while queue:
        x,y=queue.pop()
        graph[x][y]=2
        tmp=d
        if d==0:
            if graph[x][y-1]==0:
                d=3
                queue.append((x,y-1))
                cnt+=1
                continue
            if graph[x+1][y]==0:
                d=2
                queue.append((x+1,y))
                cnt+=1
                continue
            if graph[x][y+1]==0:
                d=1
                queue.append((x,y+1))
                cnt+=1
                continue
            if graph[x-1][y]==0:
                d=0
                queue.append((x-1,y))
                cnt+=1
                continue
        elif d==1:
            if graph[x-1][y]==0:
                d=0
                queue.append((x-1,y))
                cnt+=1
                continue
            if graph[x][y-1]==0:
                d=3
                queue.append((x,y-1))
                cnt+=1
                continue
            if graph[x+1][y]==0:
                d=2
                queue.append((x+1,y))
                cnt+=1
                continue
            if graph[x][y+1]==0:
                d=1
                queue.append((x,y+1))
                cnt+=1
                continue
        elif d==2:
            if graph[x][y+1]==0:
                d=1
                queue.append((x,y+1))
                cnt+=1
                continue
            if graph[x-1][y]==0:
                d=0
                queue.append((x-1,y))
                cnt+=1
                continue
            if graph[x][y-1]==0:
                d=3
                queue.append((x,y-1))
                cnt+=1
                continue
            if graph[x+1][y]==0:
                d=2
                queue.append((x+1,y))
                cnt+=1
                continue
        elif d==3:
            if graph[x+1][y]==0:
                d=2
                queue.append((x+1,y))
                cnt+=1
                continue
            if graph[x][y+1]==0:
                d=1
                queue.append((x,y+1))
                cnt+=1
                continue
            if graph[x-1][y]==0:
                d=0
                queue.append((x-1,y))
                cnt+=1
                continue
            if graph[x][y-1]==0:
                d=3
                queue.append((x,y-1))
                cnt+=1
                continue
        if tmp==d:
            if d==0 and graph[x+1][y]!=1:
                queue.append((x+1,y))
            elif d==1 and graph[x][y-1]!=1:
                queue.append((x,y-1))
            elif d==2 and graph[x-1][y]!=1:
                queue.append((x-1,y))
            elif d==3 and graph[x][y+1]!=1:
                queue.append((x,y+1))
            else:
                return cnt

            

n,m=map(int,input().split())
r,c,d=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

print(bfs(d))