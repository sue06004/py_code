import sys
input = sys.stdin.readline

class minHeap:
    def __init__(self):
        self.queue=[]
    def parent(self,index):
        return (index-1)//2
    def swap(self,i,j):
        self.queue[i],self.queue[j] = self.queue[j],self.queue[i]
    def insert(self,n):
        self.queue.append(n)
        last_Index=len(self.queue)-1
        while last_Index>=0:
            parent_Index=self.parent(last_Index)
            if parent_Index>=0 and self.queue[last_Index] < self.queue[parent_Index]:
                self.swap(last_Index,parent_Index)
                last_Index = parent_Index
            else:
                break
    def delete(self):
        last_Index=len(self.queue)-1
        if last_Index <0:
            print(0)
            return
        self.swap(0,last_Index)
        print(self.queue.pop())
        self.heapify(0)
    def heapify(self,i):
        left=2*i+1
        right=2*i+2
        min_Index=i
        if left <= len(self.queue)-1 and self.queue[min_Index] > self.queue[left]:
            min_Index = left
        if right <= len(self.queue)-1 and self.queue[min_Index] > self.queue[right]:
            min_Index = right
        if min_Index != i:
            self.swap(i,min_Index)
            self.heapify(min_Index)
N=int(input())
heapq= minHeap()
for _ in range(N):
    x=int(input())
    if x > 0:
        heapq.insert(x)
    else:
        heapq.delete()
        
