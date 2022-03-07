import sys
input = sys.stdin.readline

def bridge(n,m):
    return factorial[m]//(factorial[n]*factorial[m-n])
        

t = int(input())
factorial=[1,1] + [-1 for _ in range(29)]
for i in range(2,30):
    factorial[i] = factorial[i-1]*i

for _ in range(t):
    a,b = map(int,input().split())
    print(bridge(a,b))
    