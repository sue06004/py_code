import sys
input = sys.stdin.readine

n = int(input())
A = [0]+ list(map(int,input().split()))

d=[0]

for i in range(1,n+1):
    if A[i] > A [i-1]:
        d.append(d[i-1]+1)