import sys,heapq
input=sys.stdin.readline


N=int(input())
minHeap=[]
for _ in range(N):
    heapq.heappush(minHeap,int(input()))
result=0
while len(minHeap)>1:
    tmp=heapq.heappop(minHeap)+heapq.heappop(minHeap)
    result+=tmp
    heapq.heappush(minHeap,tmp)

print(result)