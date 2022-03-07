import sys
from collections import deque
input = sys.stdin.readline

m,n,h=map(int,input().split()) #m:가로, n:세로, h:높이

tomato3D=[]
queue=deque()
nonto=0
for k in range(h):
    tomato=[]
    for i in range(n):
        line = list(map(int,input().split()))
        for j in range(m):
            if line[j]==1:
                queue.append((k,i,j))
            elif line[j]==0:
                nonto+=1
        tomato.append(line)
    tomato3D.append(tomato)

day=0
while queue and nonto:
    L=len(queue)
    for _ in range(L):
        z,y,x=queue.popleft()
        if x>0 and tomato3D[z][y][x-1]==0:
            tomato3D[z][y][x-1]=1
            queue.append((z,y,x-1))
            nonto-=1
        if y>0 and tomato3D[z][y-1][x]==0:
            tomato3D[z][y-1][x]=1
            queue.append((z,y-1,x))
            nonto-=1
        if x<m-1 and tomato3D[z][y][x+1]==0:
            tomato3D[z][y][x+1]=1
            queue.append((z,y,x+1))
            nonto-=1
        if y<n-1 and tomato3D[z][y+1][x]==0:
            tomato3D[z][y+1][x]=1
            queue.append((z,y+1,x))
            nonto-=1
        if z>0 and tomato3D[z-1][y][x]==0:
            tomato3D[z-1][y][x]=1
            queue.append((z-1,y,x))
            nonto-=1
        if z<h-1 and tomato3D[z+1][y][x]==0:
            tomato3D[z+1][y][x]=1
            queue.append((z+1,y,x))
            nonto-=1
    day+=1
if nonto:
    print(-1)
else:
    print(day)