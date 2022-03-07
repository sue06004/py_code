import sys
input = sys.stdin.readline

def back_tracking(n,m,visited=[]):
    if len(visited)==m:
        print(" ".join(map(str,visited)))
        return
    for i in range(1,n+1):
        visited.append(i)
        back_tracking(n,m,visited)
        visited.pop()

N,M=map(int,input().split())
back_tracking(N,M)