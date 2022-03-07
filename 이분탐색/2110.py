import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def sol(start, end, remain):
    global result,home
    if remain == 0:
        return 
    mid=(start+end)//2
    if remain%2 !=0:
        result.append(home[mid])
    sol(start,mid-1,remain//2)
    sol(mid+1,end,remain//2)


n,c = map(int,input().split())
home = []
for _ in range(n):
    home.append(int(input()))
home.sort()
result=[home[0],home[-1]]
sol(0,n-1,c-2)
result.sort()
li=[]
for i in range(1,len(result)):
    li.append(result[i]-result[i-1])
print(min(li))