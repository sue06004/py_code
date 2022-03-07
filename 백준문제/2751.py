def merge(a,b):
    c=[]
    i,j=0,0
    while i!=len(a) and j!=len(b):
        if a[i]<b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
    while i!=len(a):
        c.append(a[i])
        i+=1
    while j!=len(b):
        c.append(b[j])
        j+=1
    return c 
def mergeSort(nums):
    if len(nums)==1:
        return nums
    mid = len(nums)//2    
    a=mergeSort(nums[:mid])
    b=mergeSort(nums[mid:])
    c=merge(a,b)
    return c

T=int(input())
nums=[]
for t in range(T):
    nums.append(int(input()))

print("\n".join(map(str,mergeSort(nums))))
