import sys
input = sys.stdin.readline

class heap:
    def __init__(self):
        self.queue=[]
    def parent(self,index):
        return (index-1)//2
    def swap(self,i,j):
        self.queue[i],self.queue[j]=self.queue[j],self.queue[i]
    def insert(self,n):
        self.queue.append(n)
        lastIndex=len(self.queue)-1
        while lastIndex>=0:
            parentIndex = self.parent(lastIndex)
            if parentIndex>=0 and abs(self.queue[lastIndex]) < abs(self.queue[parentIndex]):
                self.swap(lastIndex,parentIndex)
                lastIndex =parentIndex
            elif parentIndex>=0 and abs(self.queue[lastIndex]) == abs(self.queue[parentIndex]):
                if self.queue[lastIndex] < self.queue[parentIndex]:
                    self.swap(lastIndex,parentIndex)
                    lastIndex =parentIndex
                else:
                    break
            else:
                break
    def delete(self):
        lastIndex = len(self.queue)-1
        if lastIndex<0:
            print(0)
            return 
        self.swap(0,lastIndex)
        print(self.queue.pop())
        self.heapify(0)
    def heapify(self,i):
        left=2*i+1
        right=2*i+2
        minIndex=i
        if left<=len(self.queue)-1 and abs(self.queue[minIndex])>abs(self.queue[left]):
            minIndex=left
        elif left<=len(self.queue)-1 and abs(self.queue[minIndex])==abs(self.queue[left]):
            if self.queue[minIndex]>self.queue[left]:
                minIndex=left
        if right<=len(self.queue)-1 and abs(self.queue[minIndex])>abs(self.queue[right]):
            minIndex=right
        elif right<=len(self.queue)-1 and abs(self.queue[minIndex])==abs(self.queue[right]):
            if self.queue[minIndex]>self.queue[right]:
                minIndex=right
        if minIndex!=i:
            self.swap(minIndex,i)
            self.heapify(minIndex)

N=int(input())
heapq=heap()
for _ in range(N):
    x=int(input())
    if x!=0:
        heapq.insert(x)
    else:
        heapq.delete()
