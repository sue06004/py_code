import sys
input = sys.stdin.readline

def sol(n,b,li):
    if b==1:
        for i in range(n):
            for j in range(n):
                li[i][j] %= 1000
        return li
    li1=sol(n,b//2,li)
    li2=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                li2[i][k]+=li1[i][j]*li1[j][k]
        for j in range(n):
            li2[i][j]%=1000
    if b%2==0:
        return li2    
    li3=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                li3[i][k]+=li[i][j]*li2[j][k]
        for j in range(n):
            li3[i][j]%=1000
    return li3
N,B = map(int,input().split())
li=[]
for _ in range(N):
    li.append(list(map(int,input().split())))


for i in range(N):
    print(" ".join(list(map(str,sol(N,B,li)[i]))))