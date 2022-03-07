import sys
input = sys.stdin.readline

def sol(n,li):
    if len(li)==1:
        if li[0][0]=="-1":
            return (1,0,0)
        elif li[0][0]=="0":
            return (0,1,0)
        else:
            return (0,0,1)
    state = li[0][0]
    for arr in li:
        for l in arr:
            if l != state:
                a=sol(n//3,[part[:n//3] for part in li[:n//3]])
                b=sol(n//3,[part[n//3:n//3*2] for part in li[:n//3]])
                c=sol(n//3,[part[n//3*2:] for part in li[:n//3]])
                d=sol(n//3,[part[:n//3] for part in li[n//3:n//3*2]])
                e=sol(n//3,[part[n//3:n//3*2] for part in li[n//3:n//3*2]])
                f=sol(n//3,[part[n//3*2:] for part in li[n//3:n//3*2]])
                g=sol(n//3,[part[:n//3] for part in li[n//3*2:]])
                h=sol(n//3,[part[n//3:n//3*2] for part in li[n//3*2:]])
                i=sol(n//3,[part[n//3*2:] for part in li[n//3*2:]])
                return (a[0]+b[0]+c[0]+d[0]+e[0]+f[0]+g[0]+h[0]+i[0],
                        a[1]+b[1]+c[1]+d[1]+e[1]+f[1]+g[1]+h[1]+i[1],
                        a[2]+b[2]+c[2]+d[2]+e[2]+f[2]+g[2]+h[2]+i[2])
    if state=="0":
        return (0,1,0)
    elif state=="1":
        return (0,0,1)
    else:
        return (1,0,0)


n = int(input())
li = []
for _ in range(n):
    li.append(input().split())

result = sol(n,li)
print(result[0])
print(result[1])
print(result[2])