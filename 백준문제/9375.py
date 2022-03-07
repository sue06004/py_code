import sys
input = sys.stdin.readline

def combi(n,m):
    return factorial[m]//(factorial[n]*factorial[m-n])

factorial=[1,1] + [-1 for _ in range(29)]
for i in range(2,31):
    factorial[i]=factorial[i-1]*i

t = int(input())

for _ in range(t):
    n = int(input())
    di={}
    for _ in range(n):
        c,k = input().split()
        if k in di:
            di[k].append(c)
        else:
            di[k]=[c]
    result=1
    for k in di:
        result*=(combi(1,len(di[k]))+1)
    result-=1
    print(result)