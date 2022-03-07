prime=[False,False]+[True]*9999
for i in range(2,int((10001)**0.5+1)):
    for j in range(i*2,10001,i):
        prime[j]=False

T = int(input())
for t in range(T):
    n = int(input())  
    d=[]
    for x,y in enumerate(prime):
        if y:
            if prime[n-x]:
                d.append((x,n-x))
    print("%d %d" %d[(len(d)-1)//2])    
        