import sys
input = sys.stdin.readline

class Stack():
    def __init__(self):
        self.stack =[]
    def push(self,x):
        self.stack.append(x)
    def pop(self):
        if self.stack == []:
            return -1
        else:
            return self.stack.pop()
    def size(self):
        return len(self.stack)
    def empty(self):
        return 1 if self.stack==[] else 0
    def top(self):
        return -1 if self.stack==[] else self.stack[-1]


n= int(input())
stack = Stack()
for _ in range(n):
    cmd = input().split()
    if cmd[0] == "push":
        stack.push(int(cmd[1]))
    elif cmd[0] == "pop":
        print(stack.pop())
    elif cmd[0] == "size":
        print(stack.size())
    elif cmd[0] == "empty":
        print(stack.empty())
    elif cmd[0] == "top":
        print(stack.top())