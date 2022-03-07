import sys
input = sys.stdin.readline

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def dfs(graph,a,b):
    n=len(graph)
    graph[a][b]=0
    cnt=1
    for i in range(4):
        nx=a+dx[i]
        ny=b+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        if graph[nx][ny]==1:
            cnt+=dfs(graph,nx,ny)
    return cnt

n=int(input())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().strip())))

cnt=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            cnt.append(dfs(graph,i,j))
cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])