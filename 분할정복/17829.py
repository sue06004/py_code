import sys
input = sys.stdin.readline

def sol(n,li):
    if n==2:
        return sorted(li[0]+li[1])[2]
    
    a=[]
    b=[]
    c=[]
    d=[]
    for i in range(n):
        if i < n//2:
            a.append(li[i][:n//2])
            b.append(li[i][n//2:])
        else:
            c.append(li[i][:n//2])
            d.append(li[i][n//2:])
    result=[sol(n//2,a),sol(n//2,b),sol(n//2,c),sol(n//2,d)]
    return sorted(result)[2]

n=int(input())
li=[]
for _ in range(n):
    li.append(list(map(int,input().split())))

print(sol(n,li))
