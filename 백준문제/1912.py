import sys
n=int(input())
li = list(map(int,input().split()))
max_=li[0]
sum_=li[0]
for i in range(1,n):
    if sum_+li[i] > 0:
        sum_+=li[i]
        max_=max(max_,sum_)
    else:
        sum_=0
        sum_+=li[i]
        max_=max(max_,sum_)
        sum_=0
        continue
print(max_)