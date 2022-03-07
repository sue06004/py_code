import sys
input =sys.stdin.readline

n=int(input())
ground=[list(map(int,input().split())) for _ in range(n)]
mn=sys.maxsize

def solv(arr):
    global mn
    sum_=0
    if len(arr)!=len(set(arr)):
        return
    dx=[0,0,0,-1,1]
    dy=[0,-1,1,0,0]
    result=[]
    for p in arr:
        px=p//n
        py=p%n
        if px==0 or py==0 or px==n-1 or py==n-1:
            return
        for i in range(5):
            nx=px+dx[i]
            ny=py+dy[i]
            result.append((nx,ny))
            sum_+=ground[nx][ny]
    if len(set(result))!=15:
        return
    mn=min(mn,sum_)
for i in range(n**2):
    for j in range(i+1,n**2):
        for k in range(j+1,n**2):
            solv([i,j,k])
print(mn)