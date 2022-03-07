

n,k = map(int,input().split())

li = [i for i in range(1,n+1)]
result=[]
i=0
print("<",end="")
while len(li)>1:
    for _ in range(k-1):
        li.append(li.pop(0))
    print(li.pop(0),end=", ")
print(li.pop(),end=">")