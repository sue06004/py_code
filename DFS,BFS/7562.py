import sys
from collections import deque
input = sys.stdin.readline

dx=[-2,-2,-1,-1,1,1,2,2]
dy=[-1,1,-2,2,-2,2,-1,1]

t=int(input())
for _ in range(t):
    l=int(input())
    chess=[[0 for _ in range(l)] for _ in range(l)]
    now_x,now_y=map(int,input().split())
    des_x,des_y=map(int,input().split())

    queue=deque()
    queue.append((now_x,now_y))
    while queue:
        x,y=queue.popleft()
        if (x,y)==(des_x,des_y):
            print(chess[y][x])
            break
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<l and 0<=ny<l and chess[ny][nx]==0:
                chess[ny][nx]=chess[y][x]+1
                queue.append((nx,ny))
