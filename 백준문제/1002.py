T = int(input())
for t in range(T):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    r3 = ((x1-x2)**2+(y1-y2)**2)**0.5
    print(r3)
    if r3==0:
        if r1==r2:
            print(-1)
        else:
            print(0)
    else:
        if (r1+r2)>r3:
            if (r3+r2)==r1 or (r3+r1)==r2:
                print(1)
            else:
                print(2)
        elif (r1+r2)==r3:
            print(1)
        else:
            print(0)