import sys
input = sys.stdin.readline



n=int(input())
stair=[0]
for _ in range(n):
    stair.append(int(input()))
    
dp=[0]
i=1
cntContinue=0
while i < n+1:
    dp.append(stair[i])
    if i==1:
        cntContinue=1
        i+=1
        continue
    if cntContinue < 2:
        if dp[i-2]+dp[i] > dp[i-1]+dp[i]:
            dp[i]+=dp[i-2]
            cntContinue=1
            i+=1
        else:
            dp[i]+=dp[i-1]
            cntContinue+=1
            i+=1
    elif cntContinue >= 2:
        if dp[i-2]+dp[i] > dp[i-3]+stair[i-1]+dp[i]:
            dp[i]+=dp[i-2]
            cntContinue=1
            i+=1
        else:
            dp[i]+=dp[i-3]+stair[i-1]
            cntContinue=2
            i+=1
print(dp)
print(dp[-1])