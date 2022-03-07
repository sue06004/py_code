import sys
from itertools import permutations
input = sys.stdin.readline

k=int(input())
sign=input().split()
li=[0]*10
mx=0
mn=sys.maxsize

def possible(a,b,si):
    if si=="<":
        return a<b
    else:
        return a>b
def solve(s,cnt):
    global mx,mn
    if cnt==k+1:
        mx=max(mx,int(s))
        mn=min(mn,int(s))
        return
    for i in range(10):
        if li[i]==0:
            if cnt==0 or possible(int(s[-1]),i,sign[cnt-1]) :
                li[i]=1
                solve(s+str(i),cnt+1)
                li[i]=0


solve('',0)
print(mx)
if len(str(mn))==k:
    print("0"+str(mn))
else:
    print(mn)