import sys
input = sys.stdin.readline

n,m=map(int,input().split())
mon=[]
d={}
for i in range(n):
    p=input().strip()
    mon.append(p)
    d[p]=i+1
for _ in range(m):
    que=input().strip()
    if que.isalpha():
        print(d[que])
    else:
        print(mon[int(que)-1])