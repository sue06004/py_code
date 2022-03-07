import math
n,m=map(int,input().split())

factorial=math.factorial(n)
print(factorial)
mFacto=math.factorial(m)
nmFacto=math.factorial(n-m)

combination = factorial//(mFacto*nmFacto)
print(combination)
cnt=0
while combination>0:
    if combination%10==0:
        cnt+=1
        combination//=10
    else:
        break
print(cnt)

