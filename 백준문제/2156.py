n= int(input())
amount=[0]
for _ in range(n):
    amount.append(int(input()))

dp=[0]
cntContinue=0
max_=0
idx=-1
for i in range(1,n+1):
    if i == 1:
        dp.append(amount[i])
        cntContinue+=1
        max_=dp[i]
        idx=i
        continue
    dp.append(amount[i])

    if cntContinue < 2:
        dp[i]+=max_
        if i-1 == idx:
            cntContinue+=1
        else:
            cntContinue=1
        max_=dp[i]
        idx=i
    else:
        if i-1 == idx and amount[i-1]+max(dp[:i-2])> max(dp[:i-1]):
            dp[i]+=amount[i-1]+max(dp[:i-2])
            cntContinue=2
            if dp[i]>max_:
                max_=dp[i]
                idx=i
        elif i-1==idx and amount[i-1]+max(dp[:i-2]) <=max(dp[:i-1]):
            dp[i]+=max(dp[:i-1])
            cntContinue=1
            if dp[i]>max_:
                max_=dp[i]
                idx=i
        else:
            dp[i]+=max_
            max_=dp[i]
            idx=i
            cntContinue=1

print(max(dp))