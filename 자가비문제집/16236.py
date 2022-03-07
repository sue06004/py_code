import sys
from collections import deque
input = sys.stdin.readline
dx=[0,-1,1,0]
dy=[-1,0,0,1]
def bfs(sy,sx):
    queue=deque()
    queue.append((sy,sx))
    visit=[[-1]*n for _ in range(n)]
    visit[sy][sx]=0
    tm=1
    flag=0
    result=[]
    while queue:
        if flag==1:
            break
        for _ in range(len(queue)):
            y,x=queue.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<n and 0<=ny<n and visit[ny][nx]==-1:
                    if graph[ny][nx]==0:
                        queue.append((ny,nx))
                        visit[ny][nx]=tm
                    elif shark > graph[ny][nx]:
                        flag=1
                        result.append((ny,nx,tm))
                    elif shark == graph[ny][nx]:
                        queue.append((ny,nx))
                        visit[ny][nx]=tm
        tm+=1
    if result:
        a,b,c=n,n,0
        for i,j,k in result:
            if i<a:
                a,b,c=i,j,k
            elif i==a and b>j:
                a,b,c=i,j,k
        graph[sy][sx]=0
        graph[a][b]=9
        return (a,b,c)
    return (-1,-1,-1)
n=int(input())
graph=[list(map(int,input().split())) for _ in range(n)]

y,x=0,0
flag=0
for i in range(n):
    for j in range(n):
        if graph[i][j]==9:
            y,x=i,j
            flag=1
            break
    if flag==1:
        break

shark=2
cnt=0
time=0
tmp=0
while True:
    y,x,t=bfs(y,x)
    if y==-1:
        break
    cnt+=1
    time+=t
    if cnt==shark:
        shark+=1
        cnt=0
print(time)

