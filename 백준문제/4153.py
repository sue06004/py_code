while True:
    a,b,c = map(int,input().split())
    if (a,b,c) == (0,0,0):
        break
    li = sorted(list([a,b,c]))
    if li[2]**2==(li[0]**2+li[1]**2):
        print("right")
    else:
        print("wrong")