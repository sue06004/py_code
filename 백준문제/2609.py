

x,y=map(int,input().split())

min_=0
i=min(x,y)//2
if max(x,y)%min(x,y)==0:
    min_=min(x,y)
else:
    while True:
        if x%i==0 and y%i==0:
            min_=i
            break
        else:
            i-=1

i,j=2,2
a,b=x,y
while True:
    if a<b:
        a=x*i
        i+=1
    elif a>b:
        b=y*j
        j+=1
    else:
        break

print(min_)
print(a)
