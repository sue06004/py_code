import sys,heapq
input = sys.stdin.readline

n = int(input())
minHeap=[]
times=[]
cnt=0
for _ in range(n):
    heapq.heappush(minHeap,list(map(int,input().split())))
for i in range(n):
    if i==0:
        heapq.heappush(times,heapq.heappop(minHeap)[1])
        cnt+=1
        continue
    if times[0] <= minHeap[0][0]:
        heapq.heappop(times)
        heapq.heappush(times,heapq.heappop(minHeap)[1])
    else:
        heapq.heappush(times,heapq.heappop(minHeap)[1])
        cnt+=1
print(cnt)    