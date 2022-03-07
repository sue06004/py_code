import sys
input = sys.stdin.readline

n = int(input())
triNum= []
for _ in range(n):
    triNum.append(list(map(int,input().split())))

triSum=[[-1 for _ in range(len(li))] for li in triNum]
row,col = n-1,0
while row >=0:
    if row == n-1:
        for j in range(len(triNum[row])):
            triSum[row][j] = triNum[row][j]
        row-=1
        continue
    for  col in range(len(triNum[row])):
        triSum[row][col]= triNum[row][col]+max(triSum[row+1][col],triSum[row+1][col+1])
    row-=1
print(triSum[0][0])      
        