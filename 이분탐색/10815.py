import sys
input = sys.stdin.readline

n = int(input())
cardsHave = list(map(int,input().split()))
m = int(input())
nums = list(map(int,input().split()))

cardsHave.sort()

for i in nums:
    start,end = 0,n-1
    result = 0
    while start<=end:
        mid = (start+end)//2
        if cardsHave[mid] > i:
            end = mid-1
        elif cardsHave[mid] < i:
            start= mid+1
        else:
            print(1,end=" ")
            result = 1
            break
    if result ==0:
        print(0,end = " ")