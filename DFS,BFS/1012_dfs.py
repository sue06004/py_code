import sys
input = sys.stdin.readline

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def dfs(graph,y,x):
    n_x=len(graph[0])
    n_y=len(graph)
    graph[y][x]=0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>=n_x or ny<0 or ny>=n_y:
            continue
        if graph[ny][nx]==1:
            dfs(graph,ny,nx)

T=int(input())
for _ in range(T):
    m,n,k=map(int,input().split())
    graph=[[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x,y=map(int,input().split())
        graph[y][x]=1
    cnt=0
    for i in range(n): #i는 세로
        for j in range(m):#j는 가로
            if graph[i][j]==1:
                dfs(graph,i,j)
                cnt+=1
    print(cnt)