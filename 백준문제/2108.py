import sys
import collections

T=int(sys.stdin.readline())
nums= []
for i in range(T):
    nums.append(int(sys.stdin.readline()))

nums.sort()
print("%.0f" %(sum(nums)/len(nums)))
print("%d" %nums[len(nums)//2])
if T == 1:
    print(nums[0])
else:
    m = collections.Counter(nums).most_common(2)
    if m[0][1] == m[1][1]:
        print(m[1][0])
    else:
        print(m[0][0])

print(max(nums)-min(nums))