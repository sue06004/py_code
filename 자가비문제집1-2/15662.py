import sys
input = sys.stdin.readline

def rotate(n,dir):
    if n<t-1:
        tmp=wheels[n][2]
        tmpdir=dir
        for i in range(n+1,t):
            if wheels[i][6]!=tmp:
                tmp=wheels[i][2]
                if tmpdir==-1:
                    wheels[i]=[wheels[i][7]]+wheels[i][:7]
                else:
                    wheels[i]=wheels[i][1:]+[wheels[i][0]]
                tmpdir*=-1
            else:
                break
    if n>0:
        tmp=wheels[n][6]
        tmpdir=dir
        for i in range(n-1,-1,-1):
            if wheels[i][2]!=tmp:
                tmp=wheels[i][6]
                if tmpdir==-1:
                    wheels[i]=[wheels[i][7]]+wheels[i][:7]
                else:
                    wheels[i]=wheels[i][1:]+[wheels[i][0]]
                tmpdir*=-1
            else:
                break
    if dir==1:
        wheels[n]=[wheels[n][7]]+wheels[n][:7]
    else:
        wheels[n]=wheels[n][1:]+[wheels[n][0]]



t=int(input())
wheels=[list(input().strip()) for _ in range(t)]

k=int(input())
rot=[]
for _ in range(k):
    start,dir=map(int,input().split())
    rotate(start-1,dir)

cnt=0
for i in range(t):
    if wheels[i][0]=="1":
        cnt+=1
print(cnt)

