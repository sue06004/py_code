import sys
from collections import deque
input = sys.stdin.readline

def sol():
    global year
    queue=deque()
    cnt=0
    tmp=[]
    for i in range(n):
        for j in range(m):
            if graph[i][j] and visit[i][j]==year:
                if cnt==1:
                    return 2
                queue.append((i,j))
                visit[i][j]+=1
                while queue:
                    x,y=queue.popleft()
                    if x>0 and visit[x-1][y]==-1 and graph[x][y]:
                        graph[x][y]-=1
                    if x<n-1 and visit[x+1][y]==-1 and graph[x][y]:
                        graph[x][y]-=1
                    if y>0 and visit[x][y-1]==-1 and graph[x][y]:
                        graph[x][y]-=1
                    if y<m-1 and visit[x][y+1]==-1 and graph[x][y]:
                        graph[x][y]-=1
                    if graph[x][y]==0:
                        tmp.append((x,y))
                    if x>0 and visit[x-1][y]==year and graph[x-1][y]:
                        visit[x-1][y]+=1
                        queue.append((x-1,y))
                    if x<n-1 and visit[x+1][y]==year and graph[x+1][y]:
                        visit[x+1][y]+=1
                        queue.append((x+1,y))
                    if y>0 and visit[x][y-1]==year and graph[x][y-1]:
                        visit[x][y-1]+=1
                        queue.append((x,y-1))
                    if y<m-1 and visit[x][y+1]==year and graph[x][y+1]:
                        visit[x][y+1]+=1
                        queue.append((x,y+1))
                cnt+=1
    for i,j in tmp:
        visit[i][j]==-1
    return cnt


n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))
year=0
visit=[[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            visit[i][j]=-1

while True:
    cnt=sol()
    if cnt>=2:
        print(year)
        break
    elif cnt==0:
        print(0)
        break
    else:
        year+=1 
