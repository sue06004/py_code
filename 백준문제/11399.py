n=int(input())
li = list(map(int,input().split()))


li.sort()

result=0
sum_=0
for i in li:
    sum_+=i
    result+=sum_
print(result)