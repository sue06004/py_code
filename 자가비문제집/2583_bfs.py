import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    graph[y][x]=1
    area=1
    while queue:
        x,y=queue.pop()
        if y>0 and graph[y-1][x]==0:
            graph[y-1][x]=1
            queue.append((x,y-1))
            area+=1
        if y<m-1 and graph[y+1][x]==0:
            graph[y+1][x]=1
            queue.append((x,y+1))
            area+=1
        if x>0 and graph[y][x-1]==0:
            graph[y][x-1]=1
            queue.append((x-1,y))
            area+=1
        if x<n-1 and graph[y][x+1]==0:
            graph[y][x+1]=1
            queue.append((x+1,y))
            area+=1
    return area

m,n,k=map(int,input().split())
graph=[[0 for _ in range(n)] for _ in range(m)]
for _ in range(k):
    x_l,y_l,x_r,y_r=map(int,input().split())
    for y in range(y_l,y_r):
        for x in range(x_l,x_r):
            graph[y][x]=1

cnt=0
li_area=[]
for i in range(m):
    for j in range(n):
        if graph[i][j]==0:
            li_area.append(bfs(j,i))
            cnt+=1
li_area.sort()

print(cnt)
print(" ".join(list(map(str,li_area))))

