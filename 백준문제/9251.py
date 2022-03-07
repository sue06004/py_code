
a = input()
b = input()
dp=[-1]*len(a)
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]: