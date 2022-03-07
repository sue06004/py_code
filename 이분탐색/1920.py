import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def binarySearch(a,start,end):
    global A
    if start>end:
        return 0
    pivot = (start+end)//2
    if a < A[pivot]:
        return binarySearch(a,start,pivot-1)
    elif a > A[pivot]:
        return binarySearch(a,pivot+1,end)
    else:
        return 1
n = int(input())
A = list(map(int,input().split()))
m = int(input())
B = list(map(int,input().split()))
A.sort()
for b in B:
    print(binarySearch(b,0,n-1))