import sys
input = sys.stdin.readline

def sol(n,li):
    if len(li)==1:
        if li[0][0]==0:
            return (1,0)
        else:
            return (0,1)
    cnt=0
    state= li[0][0]
    for arr in li:
        for i in arr:
            if i!=state:
                a=sol(n//2,[part[:n//2] for part in li[:n//2]])
                b=sol(n//2,[part[n//2:] for part in li[:n//2]])  
                c=sol(n//2,[part[:n//2] for part in li[n//2:]])  
                d=sol(n//2,[part[n//2:] for part in li[n//2:]])
                return (a[0]+b[0]+c[0]+d[0],a[1]+b[1]+c[1]+d[1])
    if state==0:
        return (1,0)
    else:
        return (0,1)

n = int(input())
li=[]
for _ in range(n):
    li.append(list(map(int,input().split())))

result= sol(n,li)
print(result[0])
print(result[1])
