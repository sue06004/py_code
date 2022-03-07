import sys
input = sys.stdin.readline

n = int(input())
words=[]

for _ in range(n):
    words.append(input().strip())
words=list(set(words))
words.sort(key=lambda x:(len(x),x))

print("\n".join(words))