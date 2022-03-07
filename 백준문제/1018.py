N,M = map(int,input().split())

whiteboard=[]
for i in range(N):
    s = input()
    whiteboard.append(list(s))

li = [2501]
for n in range(N-7):
    for m in range(M-7):
        cnt1=0
        cnt2=0
        last1="W"
        last2="B"
        for y in range(n,n+8):
            for x in range(m,m+8):
                if whiteboard[y][x] != last1:
                    cnt1 += 1
                if last1=="W":
                    last1 = "B"
                else:
                    last1 = "W"
            if last1=="W":
                last1 = "B"
            else:
                last1 = "W"
            for x in range(m,m+8):
                if whiteboard[y][x] != last2:
                    cnt2 += 1
                if last2=="W":
                    last2 = "B"
                else:
                    last2 = "W"
            if last2=="W":
                last2 = "B"
            else:
                last2 = "W"
        if li[0] > min(cnt1,cnt2):
            li.pop()
            li.append(min(cnt1,cnt2))

print(li[0])