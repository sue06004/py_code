
n = int(input())
li= list(map(int,input().split()))

stack=[]
result = [0]*n
for i,a in enumerate(li):
    if i == 0:
        stack.append((i,a))
        continue
    if stack and stack[-1][1] < a:
        while stack and stack[-1][1] < a:
            j,k=stack.pop()
            result[j]=a
        stack.append((i,a))
    else:
        stack.append((i,a))
while stack:
    result[stack.pop()[0]]=-1

print(" ".join(map(str,result)))