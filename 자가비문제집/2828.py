import sys
input = sys.stdin.readline

n,m=map(int,input().split())
j=int(input())
apples=[1]
for _ in range(3):
    apples.append(int(input()))

l=0
flag=0

for i in range(1,len(apples)):
    if apples[i]>apples[i-1]:
        if flag==0:
            l+=apples[i]-apples[i-1]-m+1
            flag=1
        elif flag==1:
            l+=apples[i]-apples[i-1]
    elif apples[i]<apples[i-1]:
        if flag==0:
            l+=apples[i-1]-apples[i]
        elif flag==1:
            l+=apples[i-1]-m+1-apples[i]
            flag=0
print(l)