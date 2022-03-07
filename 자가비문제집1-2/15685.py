from re import X
import sys
input=sys.stdin.readline

result=[]

def dragon(x,y,d,g):
    drg=[]
    drg.append((x,y))
    if d==0:
        drg.append((x+1,y))
    elif d==1:
        drg.append((x,y-1))
    elif d==2:
        drg.append((x-1,y))
    elif d==3:
        drg.append((x,y+1))

    for i in range(g):
        for j in range(len(drg)-2,-1,-1):
            if drg[j+1][0]==drg[j][0] and drg[j+1][1]<drg[j][1]:
                drg.append((drg[-1][0]-1,drg[-1][1]))
            elif drg[j+1][0]==drg[j][0] and drg[j+1][1]>drg[j][1]:
                drg.append((drg[-1][0]+1,drg[-1][1]))
            elif drg[j+1][1]==drg[j][1] and drg[j+1][0]<drg[j][0]:
                drg.append((drg[-1][0],drg[-1][1]+1))
            elif drg[j+1][1]==drg[j][1] and drg[j+1][0]>drg[j][0]:
                drg.append((drg[-1][0],drg[-1][1]-1))
    result.extend(drg)
    
n=int(input())
for _ in range(n):
    x,y,d,g=map(int,input().split())
    dragon(x,y,d,g)
result=list(set(result))
cnt=0
for i in range(len(result)):
    if (result[i][0]+1,result[i][1]) in result and (result[i][0],result[i][1]+1) in result and (result[i][0]+1,result[i][1]+1) in result:
        cnt+=1

print(cnt)
print(1)