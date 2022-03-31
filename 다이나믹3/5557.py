import sys
input = sys.stdin.readline

n=int(input())
nums=list(map(int,input().split()))

dp=[0]*21

dp2=[0]*21
dp2[nums[0]]=1

for i in range(1,n-1):
    tmp=[0]*21
    li=[]
    for j in range(0,21):
        if dp[j]==i-1:
            if j+nums[i]<=20:
                li.append(j+nums[i])
                tmp[j+nums[i]]+=dp2[j]
            if j-nums[i]>=0:
                li.append(j-nums[i])
                tmp[j-nums[i]]+=dp2[j]
    for j in li:
        dp[j]=i
    dp2=tmp
print(dp2[nums[-1]])