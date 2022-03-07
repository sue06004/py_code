n = int(input())

people_size=[]
for i in range(n):
    x,y = map(int,input().split())
    people_size.append((x,y))

cnts=[]
for a,b in people_size:
    cnt = 0
    for c,d in people_size:
        if (a<=c and b<d) or (a<c and b<=d):
            cnt += 1
    cnts.append(cnt)
'''
a=sorted(cnts)[::-1]

for i in cnts:
    print(a.index(i)+1,end=" ")
'''
for i in cnts:
    print(i+1,end=" ")
