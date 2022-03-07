import sys
from collections import deque
input=sys.stdin.readline

dx=[0,0,-1,1]
dy=[-1,1,0,0]

r,c,k=map(int,input().split())
graph=[input().strip() for _ in range(r)]
visit=[[0]*c for _ in range(r)]
visit[r-1][0]=1
cnt=0
def dfs(x,y,dist):
    global cnt
    if dist>k:
        return
    if (x,y)==(0,c-1):
        if dist==k:
            cnt+=1
        return
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<r and 0<=ny<c and visit[nx][ny]==0 and graph[nx][ny]==".":
            visit[nx][ny]=1
            dfs(nx,ny,dist+1)
            visit[nx][ny]=0

dfs(r-1,0,1)
print(cnt)
