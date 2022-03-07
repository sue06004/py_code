import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    p = input().rstrip()
    n = int(input())
    li = input().strip()[1:-1].split(",")
    if n==0: li =[]
    l,r,start=0,n-1,True
    for s in p:
        if s == "R":
            start= not start
        elif s == "D":
            if start:
                l+=1
            else:
                r-=1
    
    if l-1>r:
        print("error")
    else:
        li = li[l:r+1]
        if not start and li:
            li.reverse()
        if li:
            print("["+",".join(li)+"]")
        else:
            print("[]")