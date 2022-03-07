import sys
input = sys.stdin.readline

def P(n,li):
    if n == 1 or n==2:
        li[n]=1
        return 1
    elif li[n] or n==0:
        return li[n]
    else:
        li[n]=P(n-2,li)+P(n-3,li)
        return li[n]

T = int(input())
li=[0]*101
for _ in range(T):
    n = int(input())
    P(n,li)
    print(li[n])