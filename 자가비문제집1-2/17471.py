import sys
from collections import deque
input = sys.stdin.readline

n=int(input())
people=list(map(int,input().split()))
around=[[] for _ in range(n+1)]
for i in range(1,n+1):
    around[i]=list(map(int,input().split()))
mn=sys.maxsize
def bfs():
    queue=deque()
    queue.append(1)
    visited=[0]*(n+1)
    while queue:
        x=queue.popleft()
        