import sys
input = sys.stdin.readline


n=int(input())
dp=[[0 for _ in range(n)] for _ in range(n)] 
matrix=[]
for _ in range(n):
    matrix.append(list(map(int,input().split())))

for i in range(1,n):
    for j in range(0,n-i):
        if i==1:
            dp[j][i+j]=matrix[j][0]*matrix[j][1]*matrix[i+j][1]
            continue
        else:
            dp[j][i+j]=sys.maxsize

        for k in range(j,i+j):
            dp[j][i+j]=min(dp[j][i+j],dp[j][k]+dp[k+1][i+j]+matrix[j][0]*matrix[k][1]*matrix[i+j][1])
print(dp[0][n-1])

'''
dp[i][j]는 matrix[i]행렬부터 [j]까지 곱한값의 최소값이다.
즉 dp[0][n-1]값이 정답이 된다.
dp[0][n-1]은 
min([0]+[1~n-1]+두 행렬의 곱비용,
[0~1]+[2~n-1]+ 비용,
[0~2]+[3~n-1]+곱 비용,
...
[0~n-2]+[n-1]+곱 비용) 이다
이를 이용해서 답을 구할수있다.

'''