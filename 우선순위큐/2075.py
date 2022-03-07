import sys,heapq
input = sys.stdin.readline

n = int(input())
heap=[]
for i in range(n):
    li=list(map(int,input().split()))
    if not heap:
        for num in li:
            heapq.heappush(heap,num)
        continue
    heapq.heapify(li)
    for _ in range(n):
        if heap[0] < li[0]:
            heapq.heappop(heap)
            heapq.heappush(heap,heapq.heappop(li))
        else:
            heapq.heappop(li)
print(heapq.heappop(heap))
'''
maxHeap 으로 문제를 풀경우 메모리초과가 일어나서
minHeap 으로 문제를 해결하였다.
n크기의 heap에 지금까지 입력받은 수중 가장 큰 수 5개가
들어가 있도록 한다.
'''