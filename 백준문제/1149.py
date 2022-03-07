#1 != 2, n != n-1 

import sys
input = sys.stdin.readline
# r=0 g=1 b=2

def cal_cost(row,col):
    
    global min_street
    if min_street[row][col] !=-1:
        return min_street[row][col]
    if row==n-1:
        min_street[row][col] = color_cost[row][col]
        return min_street[row][col]
    li=[]
    for i in range(3):
        if i != col:
            li.append(i)
    min_street[row][col]= color_cost[row][col] + min(cal_cost(row+1,li[0]),cal_cost(row+1,li[1]))
    return min_street[row][col]


n=int(input())
color_cost=[]
for _ in range(n):
    color_cost.append(list(map(int,input().split())))
min_street = [[-1 for _ in range(3)] for _ in range(n)]
row,col = n-1,0
while row >=0:
    if row==n-1:
        for i in range(3):
            min_street[row][i] = color_cost[row][i]
        row-=1
        continue
    li=[]
    for i in range(3):
        if i != col:
            li.append(i)
    min_street[row][col]=color_cost[row][col]+min(min_street[row+1][li[0]],min_street[row+1][li[1]])
    if col==2:
        row -=1
        col=0
    else:
        col+=1
print(min_street)
print(min(min_street[0]))