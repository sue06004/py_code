import sys
input = sys.stdin.readline

def fibonacci(n):
    global li
    if li[n] !=0:
        return li[n]
    elif(n==0):
        li[0] = [0,1,0]
        return [0,1,0]
    elif n==1:
        li[1]=[1,0,1]
        return [1,0,1]
    else:
        a=fibonacci(n-2)
        b=fibonacci(n-1)
        li[n]=[a[0]+b[0],a[1]+b[1],a[2]+b[2]]
        return li[n]
li=[0]*41
T = int(input())
for _ in range(T):
    f = int(input())
    print(" ".join(map(str,fibonacci(f)[1:])))

