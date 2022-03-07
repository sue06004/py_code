import sys
input= sys.stdin.readline

dx=[0,0,-1,1]
dy=[-1,1,0,0]

def dfs(x,y,cnt):
    global ans
    ans=max(ans,cnt)
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<r and 0<=ny<c and alpha[ord(board[nx][ny])-ord("A")]==0:
            alpha[ord(board[nx][ny])-ord("A")]=1
            dfs(nx,ny,cnt+1)
            alpha[ord(board[nx][ny])-ord("A")]=0

r,c=map(int,input().split())
board=[list(input().strip()) for _ in range(r)]
alpha=[0]*26
alpha[ord(board[0][0])-ord("A")]=1
ans=0
dfs(0,0,1)
print(ans)