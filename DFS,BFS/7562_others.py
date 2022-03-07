import sys
from collections import deque
input = sys.stdin.readline

def solve():
    t=int(input())
    for _ in range(t):
        l=int(input())
        chess=[[False]*l for _ in range(l)] #for문보다 빠름
        now_x,now_y=map(int,input().split())
        des_x,des_y=map(int,input().split())
        chess[now_y][now_x]=True

        queue=deque()
        queue.append((now_x,now_y))
        cnt=0
        while not chess[des_y][des_x]:
            L=len(queue)
            for _ in range(L):
                x,y=queue.popleft()
                if x-2>=0 and y-1>=0 and not chess[y-1][x-2]:
                    chess[y-1][x-2]=True
                    queue.append((x-2,y-1))
                if x-2>=0 and y+1<l and not chess[y+1][x-2]:
                    chess[y+1][x-2]=True
                    queue.append((x-2,y+1))
                if x-1>=0 and y-2>=0 and not chess[y-2][x-1]:
                    chess[y-2][x-1]=True
                    queue.append((x-1,y-2))
                if x-1>=0 and y+2<l and not chess[y+2][x-1]:
                    chess[y+2][x-1]=True
                    queue.append((x-1,y+2))
                if x+1<l and y-2>=0 and not chess[y-2][x+1]:
                    chess[y-2][x+1]=True
                    queue.append((x+1,y-2))
                if x+1<l and y+2<l and not chess[y+2][x+1]:
                    chess[y+2][x+1]=True
                    queue.append((x+1,y+2))
                if x+2<l and y-1>=0 and not chess[y-1][x+2]:
                    chess[y-1][x+2]=True
                    queue.append((x+2,y-1))
                if x+2<l and y+1<l and not chess[y+1][x+2]:
                    chess[y+1][x+2]=True
                    queue.append((x+2,y+1))
            cnt+=1
        print(cnt)

solve()
#함수화 시키는게 더 빠름.. 왜?
#파이썬은 함수를 만들때, 
#들여쓰기로 구분된 함수내부 코드들을 최적화된 코드로 변화시킨다.