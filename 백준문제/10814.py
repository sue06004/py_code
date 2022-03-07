import sys
input = sys.stdin.readline

n=int(input())
members =[]

for _ in range(n):
    members.append(input().split())

members.sort(key=lambda m:(int(m[0])))
print("\n".join(f"{age} {name}" for age,name in members))