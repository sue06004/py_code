import sys
from collections import deque
input = sys.stdin.readline

def sharkmove():
    global sharks
    tmp=[]
    for i in range(len(sharks)):
        y,x=sharks[i][0],sharks[i][1]
        s,d,z=graph[y][x].popleft()
        ny,nx,nd=moving(y,x,s,d)
        graph[ny][nx].append([s,nd,z])
        if [ny,nx] not in tmp:
            tmp.append([ny,nx])
    sharks=tmp
    for i in range(len(sharks)):
        y,x=sharks[i][0],sharks[i][1]
        if len(graph[y][x])>1:
            tmp=graph[y][x].popleft()
            li=[]
            for _ in range(len(graph[y][x])):
                li=graph[y][x].popleft()
                if tmp[2]<li[2]:
                    tmp=li
            graph[y][x].append(tmp)
def moving(y,x,s,d):
    while s>0:
        if d==1:
            if y>0:
                y-=1
                s-=1
            else:
                y+=1
                s-=1
                d=2
        elif d==2:
            if y<r-1:
                y+=1
                s-=1
            else: 
                y-=1
                s-=1
                d=1
        elif d==3:
            if x<c-1:
                x+=1
                s-=1
            else:
                x-=1
                s-=1
                d=4
        elif d==4:
            if x>0:
                x-=1
                s-=1
            else:
                x+=1
                s-=1
                d=3
    return (y,x,d)

r,c,m=map(int,input().split())
graph=[[deque() for _ in range(c)] for _ in range(r)]

sharks=[]
for _ in range(m):
    y,x,s,d,z=map(int,input().split())
    graph[y-1][x-1].append([s,d,z]) #d: 1:위,2아래,3:오른,4:왼
    sharks.append([y-1,x-1])
size=0
for i in range(c):
    for j in range(r):
        if graph[j][i]:
            size+=graph[j][i].popleft()[2]
            sharks.remove([j,i])
            break
    sharkmove()
print(size)