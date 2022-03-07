import sys
input =sys.stdin.readline

n=int(input())
ground=[list(map(int,input().split())) for _ in range(n)]
visit=[[0]*n for _ in range(n)] 
mn=sys.maxsize

def possible(x,y):
    if visit[x][y]!=0:
        return False
    if x+1>=n or visit[x+1][y]!=0:
        return False
    if x-1<0 or visit[x-1][y]!=0:
        return False
    if y+1>=n or visit[x][y+1]!=0:
        return False
    if y-1<0 or visit[x][y-1]!=0:
        return False
    return True

def sow(x,y):
    global price
    visit[x][y]=1
    visit[x+1][y]=1
    visit[x-1][y]=1
    visit[x][y+1]=1
    visit[x][y-1]=1
    price+=(ground[x][y]+ground[x+1][y]+ground[x-1][y]+ground[x][y+1]+ground[x][y-1])

def notsow(x,y):
    global price
    visit[x][y]=0
    visit[x+1][y]=0
    visit[x-1][y]=0
    visit[x][y+1]=0
    visit[x][y-1]=0
    price-=(ground[x][y]+ground[x+1][y]+ground[x-1][y]+ground[x][y+1]+ground[x][y-1])

for ix in range(n):
    for iy in range(n):
        price=0
        if possible(ix,iy):
            sow(ix,iy)
            for jx in range(n):
                for jy in range(n):
                    if possible(jx,jy):
                        sow(jx,jy)
                        for kx in range(n):
                            for ky in range(n):
                                if possible(kx,ky):
                                    sow(kx,ky)
                                    mn=min(mn,price)
                                    notsow(kx,ky)
                        notsow(jx,jy)
            notsow(ix,iy)

print(mn)