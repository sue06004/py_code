import sys
input = sys.stdin.readline

dwarf=[]
for _ in range(9):
    dwarf.append(int(input()))
dwarf.sort()

except_idx=[]
for i in range(8):
    total=sum(dwarf)
    total-=dwarf[i]
    for j in range(i+1,9):
        if total-dwarf[j]==100:
            except_idx=[i,j]
            break
    if except_idx:
        break

for i in range(9):
    if i not in except_idx:
        print(dwarf[i])