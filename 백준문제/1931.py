import sys
input = sys.stdin.readline

n = int(input())
li=[]
for _ in range(n):
    li.append(list(map(int,input().split())))

li.sort(key= lambda x: (x[1],x[0]))
print(li)

result=[]
for i in range(n):
    if i == 0:
        result.append(li[i])
        continue
    if li[i][0] >= result[-1][1]:
        result.append(li[i])
        continue
print(result)
print(len(result))