
import sys
input = sys.stdin.readline

n= int(input())
locs=[]

for _ in range(n):
    x,y = map(int,input().split())
    locs.append((x,y))

locs.sort(key=lambda loc:(loc[1],loc[0]))
#for i in range(n):
#    print(locs[i][0],locs[i][1])
print("\n".join(f"{x} {y}" for x,y in locs))