

def balance(s):
    stack = []
    for i in s:
        if i in"([":
            stack.append(i)
        elif i ==")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                print("no")
                return
        elif i =="]":
            if stack and stack[-1]=="[":
                stack.pop()
            else:
                print("no")
                return
    if stack:
        print("no")
    else:
        print("yes")

while True:
    s = input().rstrip()
    if s==".":
        break
    balance(s)
