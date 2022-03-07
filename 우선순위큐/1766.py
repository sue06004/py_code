import sys
import heapq
input = sys.stdin.readline

N,M=map(int,input().split())
condition=[]
minHeap=[]

for _ in range(M):
    a,b=map(int,input().split())
    heapq.heappush(condition,([b,a]))
for i in range(1,N+1):
    heapq.heappush(minHeap,i)
tmp_except=[] 
for i in range(1,N+1):
    pro=heapq.heappop(minHeap)
    a=pro
    tmp=[]
    while condition:
        if condition and a == condition[0][0]:
            a=condition[0][1]
            tmp.append(condition[0][1])
            heapq.heappop(condition)
            continue
        else:
            break
    for j in tmp[-1::-1]:
        if j not in tmp_except:
            print(j,end=" ")
    tmp_except+=tmp
    if pro in tmp_except:
        continue
    print(pro,end=" ")
    tmp_except.append(pro)

