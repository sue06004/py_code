
n,m = map(int,input().split())
li = list(map(int,input().split()))

deque = [i for i in range(1,n+1)]

cnt = 0
i=0
while i<m:
    if li[i] == deque[0]:
        i+=1
        deque.pop(0)
    else:
        if li[i] in deque[len(deque)//2+1:]:
            cnt+=1
            deque.insert(0,deque.pop())
        else:
            cnt+=1
            deque.append(deque.pop(0))
print(cnt)
            