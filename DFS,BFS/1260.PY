import sys
import collections
input = sys.stdin.readline

def bfs(graph,start):
    visit=[]
    queue=[]
    queue.append(start)
    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])
    return visit

def dfs(graph,start):
    visit=[]
    stack=[]
    stack.append(start)
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node][::-1])
    return visit

N,M,V=map(int,input().split())
graph=collections.defaultdict(list)
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

print(" ".join(map(str,dfs(graph,V))))
print(" ".join(map(str,bfs(graph,V))))