import sys
from collections import deque
input = sys.stdin.readline

n=int(input())
k=int(input())
board=[[0]*n for _ in range(n)]
for _ in range(k):
    ay,ax=map(int,input().split())
    board[ay-1][ax-1]=1
board[0][0]=2

l=int(input())
trans=[]
for _ in range(l):
    trans.append(input().split())

look=[0,1,2,3] #0:오른, 1:아래, 2: 왼, 3:위

dir=0
time=0

queue=deque()
queue.append((0,0))
i=0
while queue:
    time+=1
    if i<len(trans) and int(trans[i][0])==time-1:
        if trans[i][1]=='D':
            dir=(dir+1)%4
        if trans[i][1]=="L":
            dir=(dir+3)%4
        i+=1
    y,x=queue[-1]
    if dir==0:
        if x+1<n and board[y][x+1]!=2: 
            if board[y][x+1]==0:
                dely,delx=queue.popleft()
                board[dely][delx]=0
            board[y][x+1]=2
            queue.append((y,x+1))
        else:
            break
    elif dir==1:
        if y+1<n and board[y+1][x]!=2:
            if board[y+1][x]==0:
                dely,delx=queue.popleft()
                board[dely][delx]=0
            board[y+1][x]=2
            queue.append((y+1,x))
        else:
            break
    elif dir==2:
        if 0<=x-1 and board[y][x-1]!=2:
            if board[y][x-1]==0:
                dely,delx=queue.popleft()
                board[dely][delx]=0
            board[y][x-1]=2
            queue.append((y,x-1))
        else:
            break
    else:
        if 0<=y-1 and board[y-1][x]!=2:
            if board[y-1][x]==0:
                dely,delx=queue.popleft()
                board[dely][delx]=0
            board[y-1][x]=2
            queue.append((y-1,x))
        else:
            break
print(time)