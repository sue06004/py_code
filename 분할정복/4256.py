import sys
input = sys.stdin.readline

def sol(preorder,inorder):
    if not preorder:
        return
    idx = inorder.index(preorder[0])
    sol(preorder[1:idx+1],inorder[:idx])
    sol(preorder[idx+1:],inorder[idx+1:])
    print(preorder[0],end=" ")

t = int(input())
for _ in range(t):
    n=int(input())
    preorder=list(map(int,input().split()))
    inorder=list(map(int,input().split()))

    sol(preorder,inorder)
    print()