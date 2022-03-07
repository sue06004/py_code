import sys

n = int(sys.stdin.readline())
s= str(n)

li = list(map(int,s))

li.sort(reverse=True)
print("".join(map(str,li)))

