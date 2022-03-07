import sys
input = sys.stdin.readline

n=int(input())
pattern=input().strip()
li=pattern.split("*")
for _ in range(n):
    f=input().strip()
    i=0
    if li[0]==f[:len(li[0])] and li[1]==f[len(f)-len(li[1]):] and\
        len(li[0])<=len(f)-len(li[1]) :
        print("DA")
    else:
        print("NE")   

