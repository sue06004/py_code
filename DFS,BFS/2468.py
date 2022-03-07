import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue=deque()
    cnt=0
    for i in range(n):
        for j in range(n):
            if visit[i][j]==0:
                queue.append((i,j))
                visit[i][j]=1
                while queue:
                    x,y=queue.popleft()
                    if x>0 and visit[x-1][y]==0:
                        visit[x-1][y]=1
                        queue.append((x-1,y))
                    if x<n-1 and visit[x+1][y]==0:
                        visit[x+1][y]=1
                        queue.append((x+1,y))
                    if y>0 and visit[x][y-1]==0:
                        visit[x][y-1]=1
                        queue.append((x,y-1))
                    if y<n-1 and visit[x][y+1]==0:
                        visit[x][y+1]=1
                        queue.append((x,y+1))
                cnt+=1
    return cnt
n=int(input())
graph=[]
MAX=0
for _ in range(n):
    graph.append(list(map(int,input().split())))
    MAX=max(MAX,max(graph[-1]))
result=0
for h in range(MAX+1):
    visit=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] <= h:
                visit[i][j]=-1
    result=max(result,bfs())

print(result)