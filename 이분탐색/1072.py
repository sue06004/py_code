import sys
input = sys.stdin.readline

X,Y=map(int,input().split())
Z=Y*100//X 
#파이썬에서는 int(Y/x*100) 하고 Y*100//X는 값이 다른경우가 생긴다
#29/50이 그 예시이다.

start,end = 1,X
result = -1
while start<=end:
    mid = (start+end)//2
    if (Y+mid)*100//(X+mid) > Z:
        result = mid
        end=mid-1
    else:
        start=mid+1
print(result)
