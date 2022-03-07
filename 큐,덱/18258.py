
import sys
input = sys.stdin.readline

class que():
    def __init__(self):
        self.stack = [-1]*2000000
        self.left=0
        self.right=0
    def push(self,x):
        self.stack[self.right]=x
        self.right+=1
    def pop(self):
        if self.right-self.left ==0:
            return -1
        self.left+=1
        return self.stack[self.left-1]
    def size(self):
        return self.right-self.left
    def empty(self):
        return 0 if self.right-self.left>0 else 1
    def front(self):
        return self.stack[self.left] if self.right-self.left>0 else -1
    def back(self):
        return self.stack[self.right-1] if self.right-self.left>0 else -1

n = int(input())
que =que()
for _ in range(n):
    a = input().split()
    if a[0] =="push":
        que.push(int(a[1]))
    elif a[0] == "pop":
        print(que.pop())
    elif a[0] == "size":
        print(que.size())
    elif a[0] == "empty":
        print(que.empty())
    elif a[0] == "front":
        print(que.front())
    elif a[0] == "back":
        print(que.back())