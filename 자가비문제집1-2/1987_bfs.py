import sys
from collections import deque
input = sys.stdin.readline

dx=[0,0,-1,1]
dy=[-1,1,0,0]

r,c=map(int,input().split())
board=[list(input().strip()) for _ in range(r)]
ans=1
def bfs():
    global ans
    queue=set([(0,0,1,board[0][0])])
    while queue:
        x,y,count,al=queue.pop()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<r and 0<=ny<c and board[nx][ny] not in al:
                queue.add((nx,ny,count+1,al+board[nx][ny]))
                ans=max(ans,count+1)
bfs()
print(ans)