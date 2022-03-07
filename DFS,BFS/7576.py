import sys
from collections import deque
input = sys.stdin.readline

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(gph,queue):
    cnt=0
    while queue:
        tmp=list(queue)
        for y,x in tmp:
            queue.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if nx<0 or nx>=m or ny<0 or ny>=n:
                    continue
                if gph[ny][nx]==0:
                    gph[ny][nx]=1
                    queue.append((ny,nx))
        cnt+=1
    for i in range(n):
        if 0 in gph[i]:
            return -1
    return cnt-1 

m,n=map(int,input().split()) #m은 가로 n은 세로
graph=[]
tomato=deque()
for i in range(n):
    li=list(map(int,input().split()))
    for j in range(m):
        if li[j]==1:
            tomato.append((i,j))
    graph.append(li)

print(bfs(graph,tomato))
