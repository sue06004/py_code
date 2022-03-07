
import sys
input = sys.stdin.readline
#최소공배수=두자연수의 곱/최대공약수

def GCD(a,b):
    if max(a,b)%min(a,b)==0:
        return min(a,b)
    r=max(a,b)%min(a,b)
    return GCD(min(a,b),r)


t=int(input())

for _ in range(t):
    x,y=map(int,input().split())
    print(int(x*y/GCD(x,y)))