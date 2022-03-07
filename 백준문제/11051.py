
n,k=map(int,input().split())

factoLi=[1,1]+[-1 for _ in range(n-1)]

for i in range(2,n+1):
    factoLi[i]=factoLi[i-1]*i

print((factoLi[n]//(factoLi[k]*factoLi[n-k]))%10007)


