import sys
def merge(a,b):
    c=[]
    i,j=0,0
    while i<len(a) and j<len(b):
        if a[i][0] < b[j][0]:
            c.append(a[i])
            i+=1
        elif a[i][0] > b[j][0]:
            c.append(b[j])    
            j+=1
        else:
            if a[i][1] < b[j][1]:
                c.append(a[i])
                i+=1
            else:
                c.append(b[j])
                j+=1
    while i<len(a):
        c.append(a[i])
        i+=1
    while j<len(b):
        c.append(b[j])
        j+=1        
    return c
def mergeSortLoc(loc):
    if len(loc)<=1:
        return loc
    mid = len(loc)//2
    a=mergeSortLoc(loc[:mid])
    b=mergeSortLoc(loc[mid:])
    c=merge(a,b)
    return c


n= int(sys.stdin.readline())
locs=[]

for i in range(n):
    x,y = map(int,sys.stdin.readline().split())
    locs.append((x,y))
result = mergeSortLoc(locs)

for x,y in result:
    print(x,y)