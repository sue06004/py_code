import sys
from collections import deque
input = sys.stdin.readline

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(graph,i,j):
    n=len(graph)
    graph[i][j]=0
    count=1
    queue=deque()
    queue.append((i,j))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=0
                count+=1
                queue.append((nx,ny))
    return count


n=int(input())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().strip())))

cnt=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            cnt.append(bfs(graph,i,j))

cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])     
'''
먼저 시작점이 주어지지 않았으므로 이중for문으로 
1인 인덱스를 찾고 이를 bfs에 넘겨준다.
bfs는 매개변수로 전달받은 인덱스와 연결된 1들의 개수를 리턴한다.
탐색중 1인 부분은 0으로 바꿔다시 방문하지 않도록 한다.
queue에 값이 1인 인덱스정보를 저장한다.
nx,ny는 현재인덱스의 상하좌우 인덱스가 들어가서 
그 인덱스 들중에 값이 1인 인덱스를 queue에 집어넣는다.
즉 현재 인덱스에 인접한 인덱스를 queue에 넣고 count+=1을 해준다.
그리고 그 인덱스들의 값을 0으로 바꿔준다.
그런다음 처음으로 돌아가 queue에서 맨처음값을 빼서 그 값의 주변들을
조사해서 1인 값들을 queue에 넣어주는 과정을 반복한다.
'''   