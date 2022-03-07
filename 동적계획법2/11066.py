import sys
input = sys.stdin.readline


T=int(input())
for _ in range(T):
    K=int(input())
    fileSize=list(map(int,input().split()))
    dp=[[10001 for _ in range(K)] for _ in range(K)]
    result=0
    for i in range(K):
        for j in range(K-i):
            x=i+j
            if i==0:
                dp[j][x]=fileSize[j]
            for k in range(j,x):
                if i==1:
                    dp[j][x]=min(dp[j][x],dp[j][k]+dp[k+1][x])
                else:
                    dp[j][x]=min(dp[j][x],dp[j][k]+dp[k+1][x-1]+fileSize[x])
           
    print(dp)