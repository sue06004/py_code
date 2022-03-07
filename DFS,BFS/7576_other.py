import sys
from collections import deque
input = sys.stdin.readline

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(gph,queue,haveto):
    cnt=0
    while queue and haveto:
        l=len(queue)
        for _ in range(l):
            y,x=queue.popleft()
            if y<n-1 and gph[y+1][x]==0:
                gph[y+1][x]=1
                queue.append((y+1,x))
                haveto-=1
            if y>0 and gph[y-1][x]==0:
                gph[y-1][x]=1
                queue.append((y-1,x))
                haveto-=1
            if x<m-1 and gph[y][x+1]==0:
                gph[y][x+1]=1
                queue.append((y,x+1))
                haveto-=1
            if x>0 and gph[y][x-1]==0:
                gph[y][x-1]=1
                queue.append((y,x-1))
                haveto-=1
        cnt+=1
    return -1 if haveto else cnt

m,n=map(int,input().split()) #m은 가로 n은 세로
graph=[]
tomato=deque()
haveto=0
for i in range(n):
    li=list(map(int,input().split()))
    for j in range(m):
        if li[j]==1:
            tomato.append((i,j))
        elif li[j]==0:
            haveto+=1
    graph.append(li)

print(bfs(graph,tomato,haveto))
