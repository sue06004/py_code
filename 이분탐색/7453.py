import sys
input =sys.stdin.readline

n=int(input())
A,B,C,D=[0]*n,[0]*n,[0]*n,[0]*n
for i in range(n):
    li=list(map(int,input().split()))
    A[i],B[i],C[i],D[i] = li[0],li[1],li[2],li[3]
A.sort()
B.sort()
C.sort()
D.sort()

print(A,B,C,D,sep="\n")

