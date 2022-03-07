import sys
input = sys.stdin.readline

n = int(input())
li=[-1 for _ in range(501)]
li2=[-1 for _ in range(501)]

for _ in range(n):
    a,b = map(int,input().split())
    li[a]=b
    li2[b]=a

cnt1,cnt2=0,0
for i in range(501):
    if li[i]==-1:
        continue
    for j in range(i):
        if li[j] ==-1:
            continue
        if li[i] < li[j]:
            cnt1+=1
            break

for i in range(501):
    if li2[i]==-1:
        continue
    for j in range(i):
        if li2[j]==-1:
            continue
        if li2[i] < li2[j]:
            cnt2+=1
            break

print(min(cnt1,cnt2))