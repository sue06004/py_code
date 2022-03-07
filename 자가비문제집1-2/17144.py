import sys
input = sys.stdin.readline

dx=[0,0,-1,1]
dy=[-1,1,0,0]

r,c,t=map(int,input().split())
room=[]
machine=[]
for i in range(r):
    li=list(map(int,input().split()))
    if li[0]==-1:
        machine.append(i)
    room.append(li)

def spread():
    newRoom=[[0]*c for _ in range(r)]
    newRoom[machine[0]][0]=-1
    newRoom[machine[1]][0]=-1
    for i in range(r):
        for j in range(c):
            if room[i][j]>0:
                tmp=room[i][j]
                for k in range(4):
                    x=i+dx[k]
                    y=j+dy[k]
                    if 0<=x<r and 0<=y<c and room[x][y]!=-1:
                        newRoom[x][y]+=tmp//5
                        room[i][j]-=tmp//5
                newRoom[i][j]+=room[i][j]
    return newRoom

def func(ma):
    x,y=ma[0]-1,0

    while True:
        if y==0:
            if x+1==ma[0]:
                room[x][y]=0
                x-=1
            else:
                room[x+1][y],room[x][y]=room[x][y],0
                if x==0:
                    y+=1
                else:
                    x-=1
        elif x==0:
            room[x][y-1],room[x][y]=room[x][y],0
            if y==c-1:
                x+=1
            else:
                y+=1
        elif y==c-1:
            room[x-1][y],room[x][y]=room[x][y],0
            if x==ma[0]:
                y-=1
            else:
                x+=1
        elif x==ma[0]:
            room[x][y+1],room[x][y]=room[x][y],0
            if y==1:
                break
            else:
                y-=1
    x,y=ma[1]+1,0
    while True:
        if y==0:
            if x-1==ma[1]:
                room[x][y]=0
                x+=1
            else:
                room[x-1][y],room[x][y]=room[x][y],0
                if x==r-1:
                    y+=1
                else:
                    x+=1
        elif x==r-1:
            room[x][y-1],room[x][y]=room[x][y],0
            if y==c-1:
                x-=1
            else:
                y+=1
        elif y==c-1:
            room[x+1][y],room[x][y]=room[x][y],0
            if x==ma[1]:
                y-=1
            else:
                x-=1
        elif x==ma[1]:
            room[x][y+1],room[x][y]=room[x][y],0
            if y==1:
                break
            else:
                y-=1

def func2(ma):
    x,y=ma[0]-1,0

    while True:
        if y==0:
            if x+1==ma[0]:
                room[x][y]=0
                x-=1
            else:
                room[x+1][y],room[x][y]=room[x][y],0
                if x==0:
                    y+=1
                else:
                    x-=1
        elif x==0:
            room[x]=room[x][1:]+[0]
            y=c-1
            x=1
        elif y==c-1:
            room[x-1][y],room[x][y]=room[x][y],0
            if x==ma[0]:
                y-=1
            else:
                x+=1
        elif x==ma[0]:
            room[x]=[-1,0]+room[x][1:c-1]
            break
    x,y=ma[1]+1,0
    while True:
        if y==0:
            if x-1==ma[1]:
                room[x][y]=0
                x+=1
            else:
                room[x-1][y],room[x][y]=room[x][y],0
                if x==r-1:
                    y+=1
                else:
                    x+=1
        elif x==r-1:
            room[x]=room[x][1:]+[0]
            y=c-1
            x=r-2
        elif y==c-1:
            room[x+1][y],room[x][y]=room[x][y],0
            if x==ma[1]:
                y-=1
            else:
                x-=1
        elif x==ma[1]:
            room[x]=[-1,0]+room[x][1:c-1]
            break
for _ in range(t):
    room=spread()
    func2(machine)

mount=2
for i in range(r):
    mount+=sum(room[i])
print(mount)

#pypy로 제출