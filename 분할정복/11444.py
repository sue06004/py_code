
def fibo(n):
    matrix = [1,1]
    li=[0,1]
    i=1
    while i<n:
        tmp=[0,0]
        tmp[0] = matrix[0]*li[0]+matrix[1]*li[1]
        tmp[1] = matrix[0]*li[1]+matrix[1]*tmp[0]
        li=tmp
        i+=2
    return li[1]%1000000007 if i%n==0 else li[0]%1000000007

n=int(input())
print(fibo(n))


