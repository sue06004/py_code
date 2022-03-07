
k=int(input())
build=list(map(int,input().split()))

tree=[[]for _ in range(k)]

def makeTree(arr,h):
    mid=len(arr)//2
    tree[h].append(arr[mid])
    if len(arr)==1:
        return
    makeTree(arr[:mid],h+1)
    makeTree(arr[mid+1:],h+1)

makeTree(build,0)
for i in range(k):
    print(*tree[i])