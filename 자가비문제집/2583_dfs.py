import sys
input = sys.stdin.readline

dx=[0,0,-1,1]
dy=[-1,1,0,0]

def dfs(x,y):
    graph[y][x]=1
    stack=[(x,y)]
    area=1
    while stack:
        x,y=stack.pop()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[ny][nx]==0:
                stack.append((nx,ny))
                graph[ny][nx]=1
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
            li_area.append(dfs(j,i))
            cnt+=1
li_area.sort()

print(cnt)
print(" ".join(list(map(str,li_area))))