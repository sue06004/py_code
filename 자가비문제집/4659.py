import sys
input = sys.stdin.readline


while True:
    s=input().strip()
    stack=[]
    aeiou=[]
    if s=="end":
        break
    for i in range(len(s)):
        if s[i] in "aeiou":
            aeiou.append(s[i])
        if stack and stack[-1] == s[i] and s[i]!="e" and s[i]!="o":
            aeiou=[]
            break
        if stack and ((stack[-1] not in "aeiou" and s[i] in "aeiou")\
            or (stack[-1] in "aeiou" and s[i] not in "aeiou")):
            stack=[]
            stack.append(s[i])
        else:
            stack.append(s[i])
            if len(stack)==3:
                aeiou=[]
                break
    if aeiou:
        print("<"+s+"> is acceptable.")
    else:
        print("<"+s+"> is not acceptable.")