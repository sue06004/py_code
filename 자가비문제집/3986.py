import sys
input = sys.stdin.readline


n=int(input())
cnt=0
for _ in range(n):
    stack=[]
    s=input().strip()
    if len(s)%2:
        continue
    for i in s:
        if not stack:
            stack.append(i)
        else:
            if stack[-1]==i:
                stack.pop()
            else:
                stack.append(i)
    if not stack:
        cnt+=1
print(cnt)