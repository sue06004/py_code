import sys,collections
input = sys.stdin.readline

def sol(a,start,end):
    if start> end:
        return 
    mid= (start+end)//2
    if a==A[mid]:
        B_dict[a]+=1 
        if mid-1 >= start and a==A[mid-1]:
            sol(a,start,mid-1)
        if mid+1 <= end and a==A[mid+1]:
            sol(a,mid+1,end)
    elif a < A[mid]:
        sol(a,start,mid-1)
    else:
        sol(a,mid+1,end)

n=int(input())
A=list(map(int,input().split()))
m=int(input())
B=list(map(int,input().split()))
B_dict=collections.defaultdict(int)
A.sort()
for b in B:
    if B_dict[b] <= 0:
        sol(b,0,n-1)
    print(B_dict[b],end=" ")