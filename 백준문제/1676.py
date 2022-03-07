
n = int(input())
factorial=1
for i in range(2,n+1):
    factorial*=i

cnt=0
while factorial>0:
    if factorial%10==0:
        factorial//=10
        cnt+=1
        continue
    else:
        break

print(cnt)   