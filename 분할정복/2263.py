import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def sol(ia,ib,pa,pb):
    if ia>ib or pa > pb:
        return
    print(postorder[pb],end=" ")
    if ia==ib or pa == pb:
        return
    c=position[postorder[pb]]-ia
    sol(ia,ia+c-1,pa,pa+c-1)
    sol(ia+c+1,ib,pa+c,pb-1)

n = int(input())
inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))

position=[0]*(n+1)
for i in range(n):
    position[inorder[i]]=i

sol(0,n-1,0,n-1)

