import sys
input = sys.stdin.readline

n=int(input())
li=list(map(int,input().split()))

arr=[[] for _ in range(n)]
for i in range(n):
    mx,idx=0,0
    for j in range(i-1,-1,-1):
        if len(arr[j])>mx and arr[j][-1]<li[i]:
            mx=len(arr[j])
            idx=j
    if mx==0:
        arr[i]=[li[i]]
    else:
        arr[i]=arr[idx]+[li[i]]

a,b=0,0
for i in range(n):
    if len(arr[i])>a:
        a=len(arr[i])
        b=i
print(len(arr[b]))
print(*arr[b])