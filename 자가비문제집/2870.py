import sys
input = sys.stdin.readline

n=int(input())
nums=[]
left,right=-1,-1
for _ in range(n):
    line = input().strip()
    s=""
    for i in range(len(line)):
        if line[i] in "0123456789":
            s+=line[i]
        elif s:
            nums.append(int(s))
            s=""
    if s:
        nums.append(int(s))
nums.sort()
for i in nums:
    print(i)