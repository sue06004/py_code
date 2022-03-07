import sys
input = sys.stdin.readline

n,l=map(int,input().split())

hole=[]
for _ in range(n):
    hole.append(list(map(int,input().split())))
hole.sort()

cnt=0
over=0
for i in range(n): 
    if hole[i][0] <= over:
        if hole[i][1]-1<=over:
            continue
        width=hole[i][1]-(over+1)
    else:
        width=hole[i][1]-hole[i][0]
    if width%l != 0:
        cnt+=width//l+1
        over=max(hole[i][0],over+1)+(width//l+1)*l-1
    else:
        cnt+=width//l
print(cnt)