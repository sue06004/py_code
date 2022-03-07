import sys
from collections import deque
input = sys.stdin.readline

def bfs(hx,hy):
    queue=deque()
    queue.append((hx,hy))
    conv=[]
    while queue:
        x,y=queue.popleft()
        if abs(destX-x)+abs(destY-y)<=1000:
            print("happy")
            return
        for nx,ny in store:
            if (nx,ny) not in conv:
                if abs(nx-x)+abs(ny-y)<=1000:
                    queue.append((nx,ny))
                    conv.append((nx,ny))
    print("sad")

t=int(input())
for _ in range(t):
    n = int(input())
    homeX,homeY=map(int,input().split())
    store=[]
    for _ in range(n):
        store.append(list(map(int,input().split())))
    destX,destY=map(int,input().split())
    bfs(homeX,homeY)

