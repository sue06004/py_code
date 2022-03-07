from itertools import combinations
n,m=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]


home=[]
chicken=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]==2:
            chicken.append((i,j))
        elif graph[i][j]==1:
            home.append((i,j))
min_=float("inf")
comb=list(combinations(chicken,m))
for C in comb:
    dis=0
    for h in home:
        dis +=min([abs(h[0]-c[0])+abs(h[1]-c[1]) for c in C])
        if dis>=min_:
            break
    if dis<min_:
        min_=dis
print(min_)
