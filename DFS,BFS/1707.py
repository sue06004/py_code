import sys
from collections import deque
input = sys.stdin.readline
def bfs(graph,v):
    visited=[0]*(v+1)
    for i in range(1,v+1):
        if visited[i]==0:
            visited[i]=1
        else:
            continue
        queue=deque([i])
        while queue:
            a=queue.popleft()
            for j in graph[a]:
                if visited[j]==0:
                    visited[j]=-visited[a]
                    queue.append(j)
                elif visited[a]==visited[j]:
                    print("NO")
                    return
    print("YES")
def sol():
    k=int(input())
    for _ in range(k):
        v,e=map(int,input().split())
        graph=[[] for _ in range(v+1)]
        for _ in range(e):
            a,b=map(int,input().split())
            graph[a].append(b)
            graph[b].append(a)
        bfs(graph,v)        

sol()

#graph의 인덱스에 연결된 정점을 append한다.
#graph를 bfs에 전달한다.
#visited변수를 크기가 v+1인 리스트로 선언하고 0으로초기화한다
#for문으로 1부터 v+1까지 visited[i] 값을 확인하여
#방문하지않은 i를 찾는다
#visited[i]=1로 바꾸고 i를 queue에 추가한다
#queue가 비어있지않은동안 정점 i와 연결된 값들인 graph[i]
#의 값들(j)을 visited를 통해 방문했는지 확인한다
#visited[j]가 0이면 visited[i]와 반대값을 적용한다
#그리고 queue에 j를 추가한다.
#visited[j]가 0이 아니고 visited[i]와 같은 값이라면
#이분그래프가 성립하지 않으므로 NO를 출력하고 return
#38번째 줄의 for문을 통해 visited값이 전부 0이아닌데
#함수가 끝나지 않으면 이분그래프라는것으로 YES를 출력한다.