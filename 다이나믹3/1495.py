import sys
input = sys.stdin.readline

n,s,m=map(int,input().split())
volumes=list(map(int,input().split()))

dp=[-2]*(m+1)
dp[s]=-1
for i in range(n):
    tmp=[]
    for j in range(m+1):
        if dp[j]==i-1:
            if j-volumes[i]>=0:
                tmp.append(j-volumes[i])
            if j+volumes[i]<=m:
                tmp.append(j+volumes[i])
    for k in tmp:
        dp[k]=i
ans=-1
for i in range(m,-1,-1):
    if dp[i]==n-1:
        ans=i
        break
print(ans)