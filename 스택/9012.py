import sys

def vps(ps):
    stack = []
    for s in ps:
        if s=="(":
            stack.append(s)
        else:
            try:
                stack.pop()
            except:
                print("NO")
                return
    if not stack:
        print("YES")
    else:
        print("NO")

n=int(input())

for _ in range(n):
    ps = input()
    vps(ps)