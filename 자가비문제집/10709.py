import sys
input = sys.stdin.readline

H,W=map(int,input().split())
clouds=[list(input()) for _ in range(H)]
graph=[[-1 for _ in range(W)] for _ in range(H)]

for h in range(H):
    loc=-1
    for w in range(W):
        if clouds[h][w]=="c":
            graph[h][w]=0
            loc=w
        elif loc!=-1:
            graph[h][w]=w-loc

for g in graph:
    print(" ".join(list(map(str,g))))    