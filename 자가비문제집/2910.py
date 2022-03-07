import sys
from collections import Counter
input = sys.stdin.readline

n,c=map(int,input().split())
li=list(map(int,input().split()))
d=Counter(li)
li=list(d.items())
li.sort(key=lambda x:x[1],reverse=True)

for l in li:
    for j in range(l[1]):
        print(l[0],end=" ")