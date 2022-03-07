n=int(input())
m=int(input())
nums=list(map(int,input().split()))
nums.sort()
cnt=0
for i in range(n-1):
    left,right=i,len(nums)
    if nums[i]==m-nums[i]:
        continue
    while left<right:
        middle=(left+right)//2
        target=m-nums[i]
        if target<nums[middle]:
            right=middle
        elif target>nums[middle]:
            left=middle+1
        else:
            cnt+=1
            break
print(cnt)    