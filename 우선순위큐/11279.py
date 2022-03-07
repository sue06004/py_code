import sys
input = sys.stdin.readline

class maxHeap:
    def __init__(self):
        self.queue=[]
    def parent(self,index):
        return (index-1)//2
    def insert(self,n):
        self.queue.append(n)
        lastIndex=len(self.queue)-1
        while lastIndex >=0:
            parentIndex = self.parent(lastIndex)
            if parentIndex >=0 and self.queue[lastIndex] > self.queue[parentIndex]:
                self.queue[lastIndex],self.queue[parentIndex]= self.queue[parentIndex],self.queue[lastIndex]
                lastIndex=parentIndex
            else:
                break
    def delete(self):
        lastIndex = len(self.queue)-1
        if lastIndex <0:
            print(0)
            return
        self.queue[0],self.queue[lastIndex]=self.queue[lastIndex],self.queue[0]
        print(self.queue.pop())
        self.heapify(0)
    def heapify(self,i):
        leftIndex=i*2+1
        rightIndex=i*2+2
        maxIndex=i
        if leftIndex <= len(self.queue)-1 and self.queue[maxIndex] < self.queue[leftIndex]:
            maxIndex=leftIndex
        if rightIndex <= len(self.queue)-1 and self.queue[maxIndex] < self.queue[rightIndex]:
            maxIndex=rightIndex
        if maxIndex !=i:
            self.queue[maxIndex],self.queue[i] = self.queue[i],self.queue[maxIndex]
            self.heapify(maxIndex)        
N=int(input())
heapq = maxHeap()
for _ in range(N):
    x=int(input())
    if x>0:
        heapq.insert(x)
    else:
        heapq.delete()


'''
힙은 리스트로 구현된다. 
i번째 노드의 왼쪽 자식노드의 위치는 2i+1이고
i번째 노드의 오른쪽 자식 노드의 위치는 2i+2이다.
i번째 노드의 부모 노드의 위치는 (i-1)//2가 된다.
먼저 리스트를 하나 만들어 둔다.
insert(n)는 n을 리스트에 append하고 맨마지막 인덱스 부터
부모노드와의 크기를 비교하면서 부모노드보다 크면 swap하고
부모노드를 자식노드로 하여 다시 그노드의 부모노드와 비교하여 올라간다
delete()는 0번 노드와 마지막 노드를 swap하고 리스트를 pop()한뒤
heapify를 실행한다.
heapify(i)는 i인덱스 밑으로 maxheap형태로 만든다.
먼저 i인덱스의 left와 right인덱스를 구하고 이 셋중 가장큰값을
임시로 저장할 maxindex변수를 선언하고 가장 큰 인덱스를 넣는다
그리고 maxindex값이 i가아니면 heap상태가 아닌것이므로
i와 maxindex에 해당되는 값을 swap하고 maxindex밑으로 heapify인지 확인한다.
'''