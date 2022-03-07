import sys
import heapq
input = sys.stdin.readline


N=int(input())
minHeap=[]
maxHeap=[]
middle=int(input())
print(middle)
for _ in range(N-1):
    x=int(input())
    if x>middle:
        heapq.heappush(minHeap,x)
    else:
        heapq.heappush(maxHeap,-x)
    if len(minHeap)-len(maxHeap)>1:
        heapq.heappush(maxHeap,-middle)
        middle=heapq.heappop(minHeap)
    if len(maxHeap)-len(minHeap)>0:
        heapq.heappush(minHeap,middle)
        middle=-heapq.heappop(maxHeap)
    print(middle)