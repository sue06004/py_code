#풀이참고

import sys
input = sys.stdin.readline

k,n = map(int,input().split())
li=[0]*k
for i in range(k):
    li[i]=int(input())

result=0
low,high = 1,max(li)
while low<=high:
    mid = (low+high)//2
    cnt= sum([i//mid for i in li])
    if cnt >= n:
        result = mid
        low=mid+1
    elif cnt < n:
        high=mid-1

print(result)