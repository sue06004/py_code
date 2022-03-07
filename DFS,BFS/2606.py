import sys
input = sys.stdin.readline

def dfs(gr):
    global n
    visit=[0]*(n+1)
    stack=[1]
    dfs=[]
    while stack:
        node = stack.pop()
        if not visit[node]:
            visit[node]=1
            dfs.append(node)
            stack+=gr[node]
    return dfs
n=int(input())
m=int(input())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort(reverse=True)

print(len(dfs(graph))-1)