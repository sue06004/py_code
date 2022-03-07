import sys
from collections import deque
input = sys.stdin.readline

dx=[0,0,-1,1]
dy=[-1,1,0,0]
def bfs(j_x,j_y):
    if j_x==0 or j_x==c-1:
        print(1)
        return
    jihoon=deque()
    jihoon.append((j_y,j_x))
    fire=deque(fires)
    time=0
    while fire:
        time+=1
        for _ in range(len(fire)):
            fy,fx=fire.popleft()
            for i in range(4):
                nfy=fy+dy[i]
                nfx=fx+dx[i]
                if 0<=nfy<r and 0<=nfx<c and maze[nfy][nfx] in ".J":
                    maze[nfy][nfx]="F"
                    fire.append((nfy,nfx))
        if not jihoon:
            print("IMPOSSIBLE")
            return
        for _ in range(len(jihoon)):
            jy,jx=jihoon.popleft()
            for i in range(4):
                njy=jy+dy[i]
                njx=jx+dx[i]
                if 0<=njy<r and 0<=njx<c and maze[njy][njx]==".":
                    if njy==0 or njy==r-1 or njx==0 or njx==c-1:
                        print(time+1)
                        return
                    maze[njy][njx]="J"
                    jihoon.append((njy,njx))
    while jihoon:
        time+=1
        for _ in range(len(jihoon)):
            jy,jx=jihoon.popleft()
            for i in range(4):
                njy,njx=jy+dy[i],jx+dx[i]
                if 0<=njy<r and 0<=njx<c and maze[njy][njx]==".":
                    if njy==0 or njy==r-1 or njx==0 or njx==c-1:
                        print(time+1)
                        return
                    maze[njy][njx]="J"     
                    jihoon.append((njy,njx))
    print("IMPOSSIBLE")
r,c=map(int,input().split())
maze=[list(input().strip()) for _ in range(r)]
j_y,j_x=0,0
fires=[]
for i in range(r):
    for j in range(c):
        if maze[i][j]=="J":
            j_y,j_x=i,j
        elif maze[i][j]=="F":
            fires.append((i,j))
bfs(j_x,j_y)