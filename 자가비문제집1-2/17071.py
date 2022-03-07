import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue=deque()
    queue.append(n)
    if n==k:
        return 0
    end=k
    i=1
    loc[n]=0
    while queue:
        end+=i
        i+=1
        if end>5000000:
            return -1
        for _ in range(len(queue)):
            x=queue.popleft()
            for nx in (x-1,x+1,x*2):
                if 0<=nx<5000001:
                    if nx!=end:
                        queue.append(nx)
                    else:
                        return i-1
    return -1
n,k=map(int,input().split())
loc=[-1]*5000001
print(bfs())