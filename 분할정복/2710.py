import sys
input = sys.stdin.readline


N,M = map(int,input().split())
li1=[]
for _ in range(N):
    li1.append(list(map(int,input().split())))

M,K=map(int,input().split())
li2=[]
for _ in range(M):
    li2.append(list(map(int,input().split())))

li3=[[0 for _ in range(K)] for _ in range(N)]

for n in range(N):
    for m in range(M):
        for k in range(K):
            li3[n][k]+=li1[n][m]*li2[m][k]

for l in li3:
    print(" ".join(list(map(str,l))))