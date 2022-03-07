
import sys
input = sys.stdin.readline

class deque():
    def __init__(self):
        self.deque = []
    def __getitem__(self,idx):
        return self.deque[idx] if len(self.deque) > idx else -1
    def __len__(self):
        return len(self.deque)
    def appendleft(self,x):
        self.deque.insert(0,x)
    def append(self,x):
        self.deque.append(x)
    def popleft(self):
        return self.deque.pop(0) if self.deque else -1
    def pop(self):
        return self.deque.pop() if self.deque else -1
    def size(self):
        return len(self.deque)
    def empty(self):
        return 0 if self.deque else 1
    def back(self):
        return self.deque[-1] if self.deque else -1
dq = deque()

n = int(input(15))
for _ in range(n):
    com = input().split()
    if com[0] == "push_front":
        dq.appendleft(int(com[1]))
    elif com[0] == "push_back":
        dq.append(int(com[1]))
    elif com[0] == "pop_front":
        print(dq.popleft())
    elif com[0] == "pop_back":        
        print(dq.pop())
    elif com[0] == "size":
        print(len(dq))
    elif com[0] == "empty":
        print(dq.empty())
    elif com[0] == "front":
        print(dq[0])
    elif com[0] == "back":
        print(dq[len(dq)-1])