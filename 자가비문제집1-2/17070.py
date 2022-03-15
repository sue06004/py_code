import sys
from collections import deque
input = sys.stdin.readline

n=int(input())
house=[list(map(int,input().split())) for _ in range(n)]

dp=[[0 for _ in range(n)] for _ in range(n)]

def bfs():
    queue=deque()
    queue.append((0,1,1)) #2번idex 1: 가로, 2: 대각선, 3:세로
    while queue:
        x,y,s=queue.popleft()
        if s==1:
            if y<n-1 and house[x][y+1]==0 and not (y==n-2 and x<n-1):
                queue.append((x,y+1,1))
                dp[x][y+1]+=1
            if y<n-1 and x<n-1 and house[x][y+1]==0 and house[x+1][y]==0 and house[x+1][y+1]==0:
                queue.append((x+1,y+1,2))
                dp[x+1][y+1]+=1
        elif s==2:
            if y<n-1 and house[x][y+1]==0 and not (y==n-2 and x<n-1):
                queue.append((x,y+1,1))
                dp[x][y+1]+=1
            if y<n-1 and x<n-1 and house[x][y+1]==0 and house[x+1][y]==0 and house[x+1][y+1]==0:
                queue.append((x+1,y+1,2))
                dp[x+1][y+1]+=1
            if x<n-1 and house[x+1][y]==0 and not(x==n-2 and y<n-1):
                queue.append((x+1,y,3))
                dp[x+1][y]+=1
        elif s==3:
            if y<n-1 and x<n-1 and house[x][y+1]==0 and house[x+1][y]==0 and house[x+1][y+1]==0:
                queue.append((x+1,y+1,2))
                dp[x+1][y+1]+=1
            if x<n-1 and house[x+1][y]==0 and not (x==n-2 and y<n-1):
                queue.append((x+1,y,3))
                dp[x+1][y]+=1

bfs()
print(dp[n-1][n-1])