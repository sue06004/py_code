
def gcd(a,b):
    if max(a,b)%min(a,b)==0:
        return min(a,b)
    return gcd(min(a,b),max(a,b)%min(a,b))


n=int(input())

li=list(map(int,input().split()))


st= li[0]*2

for i in range(1,n):
    gcd_=gcd(st,li[i]*2)
    print("%d/%d" %(st//gcd_,li[i]*2//gcd_))
