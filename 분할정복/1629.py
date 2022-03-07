
def sol(a,b,c):
    if b==1:
        return a%c
    if b%2==0:
        r= sol(a,b//2,c)
        return r*r%c
    else:
        r=sol(a,b//2,c)
        return r*r*a%c

a,b,c=map(int,input().split())
print(sol(a,b,c))


