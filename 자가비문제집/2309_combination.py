import sys
from itertools import combinations
input = sys.stdin.readline

dwarf=[int(input()) for _ in range(9)]

result=combinations(dwarf,7)
for li in result:
    if sum(li)==100:
        print("\n".join(list(map(str,sorted(li)))))
        break