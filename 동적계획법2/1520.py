import sys
input = sys.stdin.readline

m,n=map(int,input().split())
mp=[]
dp=[[0 for _ in range(n)] for _ in range(m)]
for _ in range(m):
    mp.append(list(map(int,input().split())))

for i in range(m):
    for j in range(n):
        for k in range(i,m):    
            if k==0 and j == 0:
                dp[k][j]=1
                continue
            tmp=[]
            if k>0 and mp[k][j] < mp[k-1][j]:  
                tmp.append(dp[k-1][j])
            if k<m-1 and mp[k][j] < mp[k+1][j]:
                tmp.append(dp[k+1][j])
            if j>0 and mp[k][j] < mp[k][j-1]:
                tmp.append(dp[k][j-1])
            if j<n-1 and mp[k][j] < mp[k][j+1]:
                tmp.append(dp[k][j+1])
            dp[k][j]=sum(tmp)
print(dp[m-1][n-1])