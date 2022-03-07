T=int(input())
nums=[]
for t in range(T):
    nums.append(int(input()))

for i in range(T):
    for j in range(i+1,T):
        if nums[i] > nums[j]:
            nums[i],nums[j] = nums[j],nums[i]

print("\n".join(map(str,nums)))