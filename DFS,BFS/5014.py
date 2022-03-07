from collections import deque

def bfs():
    queue=deque([s])
    visit=[-1]*(f+1)
    visit[s]=0
    while queue:
        y=queue.popleft()
        if y==g:
            print(visit[y])
            return
        if y<=f-u and visit[y+u]==-1:
            visit[y+u]=visit[y]+1
            queue.append(y+u)
        if y>=1+d and visit[y-d]==-1:
            visit[y-d]=visit[y]+1
            queue.append(y-d) 
    print("use the stairs")
f,s,g,u,d=map(int,input().split())
bfs()