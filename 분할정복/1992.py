import sys
input = sys.stdin.readline

def sol(n,li):
    if len(li)==1:
        if li[0][0]=="0":
            return 0
        else:
            return 1
    state=li[0][0]
    for arr in li:
        for i in arr:
            if i != state:
                a=sol(n//2,[part[:n//2] for part in li[:n//2]])
                b=sol(n//2,[part[n//2:] for part in li[:n//2]])  
                c=sol(n//2,[part[:n//2] for part in li[n//2:]])  
                d=sol(n//2,[part[n//2:] for part in li[n//2:]])
                return "("+str(a)+str(b)+str(c)+str(d)+")"
    if state=="0":
        return 0
    else:
        return 1


n=int(input())
li=[]
for _ in range(n):
    li.append(input().strip())
print(sol(n,li))