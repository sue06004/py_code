import sys
input = sys.stdin.readline

def sol(li):
    if not li:
        return 0
    if len(li)==1:
        li[0]-=9
        if li[0]<=0:
            li.pop()
        return sol(li)+1
    elif len(li)==2:
        li.sort()
        li[1]-=9
        li[0]-=3
        if li[1]<=0:
            li.pop()
        if li[0]<=0:
            li.pop(0)
        return sol(li)+1
    elif len(li)==3:
        li.sort()
        li2=[i for i in li]
        li[2]-=9
        li[1]-=3
        li[0]-=1
        li2[2]-=9
        li2[0]-=3
        li2[1]-=1
        if li[2]<=0:
            li.pop(2)
        if li[1]<=0:
            li.pop(1)
        if li[0]<=0:
            li.pop(0)
        a=sol(li)+1
        if li2[2]<=0:
            li2.pop(2)
        if li2[1]<=0:
            li2.pop(1)
        if li2[0]<=0:
            li2.pop(0)
        b=sol(li2)+1
        return min(a,b)
n=int(input())
healths=list(map(int,input().split()))

print(sol(healths))