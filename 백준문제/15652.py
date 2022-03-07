import sys
input = sys.stdin.readline

def back_track(n,m,visited=[]):
    if len(visited)==m:
        print(" ".join(map(str,visited)))
        return
    for i in range(1,n+1):
        if visited==[] or i >= visited[-1]:
            visited.append(i)
            back_track(n,m,visited)
            visited.pop()


N,M=map(int,input().split())
back_track(N,M)