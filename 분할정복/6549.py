
import sys
input = sys.stdin.readline

def sol(n,li):
    if len(n)==1:
        return li[0]
    result = [sol(li[:n//2]),sol(li[n//2:])]
    


while True:
    n = list(map(int,input().split()))
    if n == [0]:
        break
    histogram = n[1:]
    sol(historgram)