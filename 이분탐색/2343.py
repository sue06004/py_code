import sys
input = sys.stdin.readline

def sol():
    cnt=0
    addLectures=0
    for i in range(N):
        if addLectures+lectures[i] > mid:
            cnt+=1
            addLectures=0
        addLectures+=lectures[i]
    if addLectures:
        cnt+=1
    return cnt

N,M=map(int,input().split())
lectures=list(map(int,input().split()))

left,right = max(lectures),sum(lectures) #블루레이 크기의 최소/최대
result = 0
while left<=right:
    mid = (left+right)//2
    cnt = sol()
    if cnt > M:
        left = mid+1
    else: 
        result = mid 
        right = mid-1
print(result)

'''
 블루레이 크기를 찾아야 하므로 블루레이크기를 이분탐색으로 찾아야한다
 이때 초기 left값과 right값을 블루레이 크기의 최소,최대로 해야
 우리가 원하는 값을 찾아나갈 수 있다.
 lectures값을 앞에서부터 더해서 mid값보다 크면 이전값까지를
 1개의 블루레이로 하고 다시 더해가서 블루레이 크기가 mid값보다 크지 않도록
 했을 때의 블루레이 개수를 구한다.
 구한 개수를 M과 비교하여 M보다 작거나 같으면 mid값이 커서 블루레이 크기가 크다는 것으로
 right=mid-1로 하고 이때의 mid값을 result에 임시로 저장한다. 작거나 같을 때 mid값을
 임시로 저장하는 이유는 우리가 구하는 값은 블루레이 크기의 최소값이므로 cnt=M이면서 크기는 작은
 경우가 있을 수 있기 때문이다.
 M보다 크면 mid값이 작아 블루레이 개수가 많이 나온것이므로
 left=mid+1로 하고 다시 mid값을 구하여 블루레이개수를 구해 비교한다.
해설:
https://deok2kim.tistory.com/109
'''