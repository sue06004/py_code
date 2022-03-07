import sys
from collections import deque
input = sys.stdin.readline

n,k=map(int,input().split())
MAX=10**5
dist=[-1 for _ in range(MAX+1)]
dist[n]=0
def bfs(n,k):
    queue=deque()
    queue.append(n)
    while queue:
        x=queue.popleft()
        if x==k:
            print(dist[x])
            break
        if 0<=x-1<=MAX and dist[x-1] ==-1:
            dist[x-1]=dist[x]+1
            queue.append(x-1)
        if x+1<=MAX and dist[x+1] ==-1:
            dist[x+1]=dist[x]+1
            queue.append(x+1)
        if 2*x<=MAX and dist[2*x]==-1:
            dist[2*x]=dist[x]+1
            queue.append(2*x)      
bfs(n,k)

#x-1 x+1 x*2 순으로 해야 한다. 안그러면 틀린다.

        