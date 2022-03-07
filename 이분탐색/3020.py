import sys
input = sys.stdin.readline

N,H=map(int,input().split())
floor=[]
ceiling=[]

for i in range(0,N):
    t=int(input())
    if i%2==0:
        floor.append(t)
    else:
        ceiling.append(t)

minBreak=[2000000,0]
cnt=0 

floor.sort()
ceiling.sort()

for i in range(1,H+1):
    start,end=0,N//2-1
    resultf=-1
    while start<=end:
        mid = (start+end)//2
        if i > floor[mid]:
            resultf = mid 
            start= mid+1
        else:
            end=mid-1
    start,end=0,N//2-1
    resultc=-1
    while start<=end:
        mid=(start+end)//2
        if H-i+1 > ceiling[mid]:
            resultc=mid
            start=mid+1
        else:
            end=mid-1
    
    Break=N//2-1-resultf+N//2-1-resultc
    if minBreak[0] > Break:
        minBreak[0]=Break
        minBreak[1]=1
    elif minBreak[0]==Break:
        minBreak[1]+=1
print(minBreak[0],minBreak[1])