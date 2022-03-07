import sys
input = sys.stdin.readline

n = int(input())
nums= list(map(int,input().split()))

numsSort=sorted(list(set(nums)))
dic={}
for i,num in enumerate(numsSort):
    dic[num]=dic.get(num,i) #dic[num]이 존재하면 그 값을 불러오고 없으면 i로 대체한다.
    #dic.get(value,default)
print(" ".join([str(dic[i]) for i in nums]))