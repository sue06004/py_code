import sys
input = sys.stdin.readline

def sol(l,w,h,cube):
    if not cube or min(l,w,h)<=0:
        return
    global cnt
    length = 2**cube[-1][0]
    if length <= min(l,w,h):
        cube[-1][1]-=1
        cnt+=1
        if cube[-1][1]==0:
            cube.pop()
        sol(l,w,h-length,cube)
        sol(l,w-length,h,cube)
        sol(l-length,w,h,cube)
    else:
        cube.pop()
        sol(l,w,h,cube)

l,w,h = map(int,input().split())
n = int(input())
cube=[]
cnt =0
for i in range(n):
    a,b=map(int,input().split())
    cube.append([a,b])

sol(l,w,h,sorted(cube))
print(cnt)






