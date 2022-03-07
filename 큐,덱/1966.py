
import sys
input =sys.stdin.readline

t = int(input())
for _ in range(t):
    n,m=map(int,input().split())
    importance= list(map(int,input().split())) 
    cnt=0
    while True:
        if len(importance)==1:
            cnt+=1
            break
        elif importance[0] < max(importance[1:]):
            importance.append(importance.pop(0))
            m-=1
            if m < 0:
                m=len(importance)-1
        else:
            cnt+=1
            if m ==0:
                break
            importance.pop(0)
            m-=1
    print(cnt)