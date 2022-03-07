import sys
from  itertools import permutations
input =sys.stdin.readline

def rot(arr,r,c,s):
    for i in range(1,s+1):
        tmp=arr[r-i][c-i]
        y,x=r-i+1,c-i
        while y<=r+i:
            arr[y-1][x]=arr[y][x]
            y+=1
        y=r+i
        arr[y][x:c+i+1]=arr[y][x+1:c+i+1]+[0]
        y,x=r+i-1,c+i
        while r-i<=y:
            arr[y+1][x]=arr[y][x]
            y-=1
        y=r-i
        arr[y][c-i+1:x+1]=[tmp]+arr[y][c-i+1:x]
    return arr
n,m,k=map(int,input().split())
ARR=[list(map(int,input().split())) for _ in range(n)]


rotate=[]
for _ in range(k): 
    r,c,s=map(int,input().split())
    rotate.append((r-1,c-1,s))

permuLi=list(permutations(rotate,k))

mn=sys.maxsize

for i in range(len(permuLi)):
    tmp=[ARR[t][:] for t in range(n)]
    for j in range(k):
        tmp=rot(tmp,permuLi[i][j][0],permuLi[i][j][1],permuLi[i][j][2])
    for j in range(n):
        mn=min(mn,sum(tmp[j]))

print(mn)