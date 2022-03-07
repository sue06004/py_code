import sys
input = sys.stdin.readline
# + - * /
def back_track(n,nums,operator):
    global result,max_,min_
    if sum(operator)==0:
        if result > max_:
            max_=result
        if result < min_:
            min_=result
        return

    for i in range(4):
        if operator[i] !=0:
            operator[i]-=1
            tmp = result
            if i==0:
                result+=nums[0]
            elif i==1:
                result-=nums[0]
            elif i==2:
                result*=nums[0]
            else:
                if result<0:
                    result = -1*(abs(result)//nums[0])
                else:
                    result//=nums[0]
            back_track(n,nums[1:],operator)
            result = tmp
            operator[i]+=1

n = int(input())
nums = list(map(int,input().split()))
operator = list(map(int,input().split()))
result = nums[0]
max_= -sys.maxsize
min_ = sys.maxsize

back_track(n,nums[1:],operator)
print(max_)
print(min_)