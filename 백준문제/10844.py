n = int(input())
dp_list=[]

for i in range(n):
    if i == 0:
        li=[0,1,1,1,1,1,1,1,1,1]
        dp_list.append(li)
        continue
    li = [0 for _ in range(10)]
    for n in range(0,10):
        if n == 0:
            li[n]+=dp_list[0][1]
        elif n ==9:
            li[n]+=dp_list[0][8]
        else:
            li[n]+=dp_list[0][n-1]
            li[n]+=dp_list[0][n+1]
    dp_list.pop(0)
    dp_list.append(li)    

print(sum(dp_list[-1])%1000000000)