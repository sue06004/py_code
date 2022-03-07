import sys
T=int(input())
counter=[0]*10001

for t in range(T):
    n = int(sys.stdin.readline())
    counter[n]+=1

for i in range(10001):
    for j in range(counter[i]):
        print(i)