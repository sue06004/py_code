import sys
from collections import deque
input = sys.stdin.readline

def dfs_recursive(graph,M,visited=[]):
    if len(visited)==M:
        print(" ".join(map(str,visited)))
        return
    for i in graph:
        if i not in visited:
            visited.append(i)
            dfs(graph,M,visited)
            visited.pop()


N,M=map(int,input().split())

dfs_recursive(range(1,N+1),M)