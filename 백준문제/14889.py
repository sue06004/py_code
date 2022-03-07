import sys
input =sys.stdin.readline

def startLink(idx,cnt):
    global min_
    if cnt == n//2:
        start_score=0
        link_score=0
        
        for i in range(n):
            for j in range(n):
                if start[i] and start[j]:
                    start_score+=S[i][j]
                elif not (start[i] or start[j]):
                    link_score+=S[i][j]
    
        
        min_ = min(min_,abs(start_score-link_score))
        return
    
    for i in range(idx,n): #idx가 핵심임
        if start[i] !=1:
            start[i]=1
            startLink(i+1,cnt+1)
            start[i]=0
n = int(input())
S=[list(map(int,input().split())) for _ in range(n)]
start=[0]*n
min_= sys.maxsize
startLink(0,0)
print(min_)