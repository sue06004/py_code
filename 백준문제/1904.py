import sys
import collections
input = sys.stdin.readline
'''
def tile(n,li):
    global cnt
    if len(li)>n:
        return
    if len(li)==n:
        cnt+=1
        return 
    for i in [0,1]:
        if i == 0:
            li.append(0)
            li.append(0)
            tile(n,li)
            li.pop()
            li.pop()
        elif i == 1:
            li.append(1)
            tile(n,li)
            li.pop()

def tile01(n):
    global bi
    if n==1 or n==2:
        return bi[n]
    else:
        #if bi[n-1]==0:
            #tile01(n-1)
        for k in range(3,n+1):
            li=[]
            for i in bi[k-2]:
                if i+"00" not in li:
                    li.append(i+"00")
                if i+"11" not in li:
                    li.append(i+"11")
        
            for i in bi[k-1]:
                if i+"1" not in li:
                    li.append(i+"1")
            bi[k]=(li)
'''
def tile01(n):
    global bi
    if n==1 or n==2:
        return
    else:
        for i in range(3,n+1):
            bi.append(bi[1]*2+bi[0])
            bi.popleft()
        
n=int(input())
cnt=0
bi=collections.deque([1,1,2])
tile01(n)
print(bi[-1])

