N,M = map(int,input().split())
nums = list(map(int,input().split()))

result=0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            sum_=nums[i]+nums[j]+nums[k]
            if M>=sum_ and M-sum_ < M-result:
                result = sum_
print(result)
