import sys
input = sys.stdin.readline

N=int(input())
request=list(map(int,input().split()))
total=int(input())

request.sort()

start,end =0,N-1
total_n=total//N
result =0
while start<len(request):
    mid = (start+end)//2
    if request[mid] <= total//N:
        for i in range(start,mid+1):
            N-=1
            total-=request[i]
        result=mid+1
        start=mid+1
        if start > end:
            end=len(request)-1
    elif request[start] > total//N:
        break
    else:
        end=mid-1
if N!=0: 
    for i in range(result,len(request)):
        if request[i] > total//N:
            request[i]=total//N
    print(max(request[result:]))
else:
    print(max(request))