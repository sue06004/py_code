# 정답 보고 품
import sys,heapq
input = sys.stdin.readline

N,K=map(int,input().split())
jewels=[] #[무게,가치]
bags=[]
for _ in range(N):
    m,v=map(int,input().split())
    heapq.heappush(jewels,[m,v])
for _ in range(K):
    bags.append(int(input()))

bags.sort()
capacity_jewel=[] #현재 bag의 용량보다 작은 모든 보석들
result=0
for _ in range(K):
    bag= heapq.heappop(bags)
    while jewels and bag >= jewels[0][0]:
        jewel=heapq.heappop(jewels)
        heapq.heappush(capacity_jewel,-jewel[1])
    if capacity_jewel:
        result-=heapq.heappop(capacity_jewel) #capacity_jewel은 최대힙
    elif not jewels:
        break

print(result)

'''
용량이 작은 가방과 무게가 낮은 보석들부터 비교하여 가방에
들어갈 수 있는 보석들을 capacity_jewel에 최대힙으로 넣어둔다
들어갈 수 있는 보석들을 다 넣으면 result에 capacity_jewel의
최대값을 더해준다
만약 jewels와 capacity_jewel이 둘다 비어있으면 종료한다.
'''