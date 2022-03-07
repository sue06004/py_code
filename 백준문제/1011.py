#백준 1011번
T=int(input())
li=[0]
c,d,e,f=0,1,2,0
for t in range(T):
    a,b=map(int,input().split())
    r=b-a
    if r<len(li):
        print(li[r])
    else:
        for i in range(len(li),r+1):
            if i<=3:
                c=i
            else:
                if d<e:
                    d+=1
                else:
                    c+=1
                    d=1
                    f+=1
                    if f>1:
                        f=0
                        e+=1
            li.append(c)
        print(c)
                    
              
            