import sys
input = sys.stdin.readline

def sol(N,li):
    if li[0]>=0:
        print(li[0],li[1])
        return
    elif li[-1]<=0:
        print(li[-2],li[-1])
        return
    result=(10**9,10**9)
    for i in range(N):
        start,end =i+1,N-1
        while start<=end:
            mid = (start+end)//2
            if li[mid]<=0:
                start=mid+1
            else:
                if li[i]+li[mid]>0:
                    if abs(li[i]+li[mid])<abs(sum(result)):
                        result = (li[i],li[mid]) 
                    end=mid-1
                else:
                    if abs(li[i]+li[mid])<abs(sum(result)):
                        result = (li[i],li[mid]) 
                    start=mid+1
    print(result[0],result[1])

N=int(input())
values=list(map(int,input().split()))

values.sort()

sol(N,values)