import sys
input = sys.stdin.readline

n,k=map(int,input().split())
temp=list(map(int,input().split()))


sum_=sum(temp[:k])
max_=sum_
for i in range(k,n):
    sum_+=temp[i]
    sum_-=temp[i-k]
    max_=max(max_,sum_)
print(max_)