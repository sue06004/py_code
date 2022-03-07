
import sys
input = sys.stdin.readline

n = int(input())
li=[]
state = 0
for _ in range(n):
    li.append(int(input()))
    if state ==0 and len(li) != 1 and li[-2]> li[-1] and li[-1]+1  not in li:
        state=1

if state==1:
    print("NO")
else:
    i=0
    a=1
    cal =[]
    while i<n:
        if not cal:
            cal.append(a)
            print("+")
            a+=1
        if cal[-1] == li[i]:
            cal.pop()
            print("-")
            i+=1
        else:
            cal.append(a)
            print("+")
            a+=1
