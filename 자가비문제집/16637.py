import sys
from itertools import combinations
input = sys.stdin.readline

n=int(input())
susic=input().strip()
li=[]
result=0
for i in range(n):
    if i ==0:
        result+=int(susic[i])
    elif i%2!=0:
        continue
    else:
        if susic[i-1]=="*":
            result*=int(susic[i])
        elif susic[i-1]=="+":
            result+=int(susic[i])
        else:
            result-=int(susic[i])
num_cnt=(n+1)//2
max_br=num_cnt//2
br_cnt=1
while br_cnt<=max_br:
    comb=list(combinations(range(0,n-2,2),br_cnt))
    for C in comb:
        flag=0
        for i in range(len(C)-1):
            if C[i+1]-C[i]==2:
                flag=1
                break
        if flag==1:
            continue
        tmp=0
        i=0
        while i<n:
            if i in C:
                if susic[i+1]=="*":
                    a=int(susic[i])*int(susic[i+2])
                elif susic[i+1]=="+":
                    a=int(susic[i])+int(susic[i+2])
                else:
                    a=int(susic[i])-int(susic[i+2])
                if i==0 or susic[i-1]=="+":
                    tmp+=a
                elif susic[i-1]=="*":
                    tmp*=a
                else:
                    tmp-=a
                i+=4
                continue
            if i==0:
                tmp+=int(susic[i])
            elif susic[i-1]=="*":
                tmp*=int(susic[i])
            elif susic[i-1]=="+":
                tmp+=int(susic[i])
            else:
                tmp-=int(susic[i])
            i+=2
        result=max(result,tmp)
    br_cnt+=1
print(result)