n= int(input())
amount=[0]
for _ in range(n):
    amount.append(int(input()))
dp=[]
if n==1:
    dp=[0,amount[1]]
else:
    dp=[0,amount[1],amount[1]+amount[2]]+[0 for _ in range(n-2)]

for i in range(3,n+1):
    dp[i]=max(amount[i]+amount[i-1]+dp[i-3],amount[i]+dp[i-2],dp[i-1])
    

print(max(dp))