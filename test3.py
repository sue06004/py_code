from collections import deque


graph=[[deque() for _ in range(3)] for _ in range(6)]

queue=deque([1])
queue.append(1)
queue.append(2)
print(queue)
print(len(queue))