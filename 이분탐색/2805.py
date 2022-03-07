#나무자르기
import sys
input = sys.stdin.readline

n,m=map(int,input().split())
tree= list(map(int,input().split()))

low,high = 1,max(tree)
result = 0
while low<=high:
    mid = (low+high)//2
    h = 0
    for t in tree:
        if t>mid:
            h += t-mid
    if h > m:
        result = mid
        low = mid+1
    elif h < m:
        high = mid-1
    else:
        result = mid
        break
print(result)