import sys
input = sys.stdin.readline

T=int(input())
last=0
for _ in range(T):
    n=int(input())
    cnt=0
    i=5
    while i <= n:
        cnt+=n//i
        i*=5
    print(cnt)