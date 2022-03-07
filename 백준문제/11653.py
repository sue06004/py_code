n = int(input())
i=2
while i<= int(n**0.5):
    while n%i==0:
        n//=i
        print(i)
    i+=1