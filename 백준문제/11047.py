import sys
input = sys.stdin.readline

n,k = map(int,input().split())
coins =[]
for _ in range(n):
    coins.append(int(input()))

i=n-1
cnt=0
while k>0:
    if coins[i] > k:
        i-=1
    else:
        cnt+= k//coins[i]
        k=k%coins[i]
        i-=1
print(cnt)