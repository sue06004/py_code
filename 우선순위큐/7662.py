import sys,heapq
input = sys.stdin.readline

T=int(input())
for _ in range(T):
    K=int(input())
    minQ=[]
    maxQ=[]
    tmp_min=[]
    tmp_max=[]
    cnt=0
    for _ in range(K):
        op,n=input().split()
        n=int(n)
        if op == "I":
            heapq.heappush(minQ,n)
            heapq.heappush(maxQ,-n)
            cnt+=1
        else:
            if not cnt:
                minQ=[]
                maxQ=[]
                tmp_min=[]
                tmp_max=[]
                continue
            if n==-1:
                while True:
                    tmp=heapq.heappop(minQ)
                    if tmp_max and tmp == tmp_max[0]:
                        heapq.heappop(tmp_max)
                        continue
                    heapq.heappush(tmp_min,-tmp)
                    break
            else:
                while True:
                    tmp=heapq.heappop(maxQ)
                    if tmp_min and  tmp == tmp_min[0]:
                        heapq.heappop(tmp_min)
                        continue
                    heapq.heappush(tmp_max,-tmp)
                    break
            cnt-=1
    if cnt==0:
        print("EMPTY")
    else:    
        while maxQ:
            a=heapq.heappop(maxQ)
            if not tmp_min or a != heapq.heappop(tmp_min):
                print(-a,end=" ")
                break
        while minQ:
            a=heapq.heappop(minQ)
            if not tmp_max or a != heapq.heappop(tmp_max):
                print(a)
                break