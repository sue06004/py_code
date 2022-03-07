a,b,c=map(int,input().split())
x,y=[],[]
for _ in range(3):
    s,e=map(int,input().split())
    x.append(s)
    y.append(e)
x.sort()
y.sort()

i,j=0,0
cnt=0
price=0
for k in range(1,101):
    if i==3 and j==3:
        break
    while i<3 and x[i]==k:
        i+=1
        cnt+=1
    while j<3 and y[j]==k:
        j+=1
        cnt-=1
    if cnt==1:
        price+=a
    elif cnt==2:
        price+=b*2
    elif cnt==3:
        price+=c*3 
print(price)       
