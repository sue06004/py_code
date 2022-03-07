import sys
input = sys.stdin.readline

def dfs(graph,start):
    visit=[0 for _ in range(N+1)]
    dfs=[]
    stack=[start]
    while stack:
        node = stack.pop()
        if not visit[node]:
            dfs.append(node)
            visit[node]=1
            stack+=graph[node]
    return dfs

def bfs(graph,start):
    visit=[0 for _ in range(N+1)]
    queue=[start]
    bfs=[]
    while queue:
        node = queue.pop()
        if not visit[node]:
            bfs.append(node)
            visit[node]=1
            queue=graph[node][::-1]
    return bfs

N,M,V=map(int,input().split())
graph=[[] for _ in range(N+1)]
for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(N+1):
    graph[i].sort(reverse=True)

print(" ".join(map(str,dfs(graph,V))))
print(" ".join(map(str,bfs(graph,V))))