import sys
input = sys.stdin.readline

move=list(map(int,input().split()))

scores=[[2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40],\
    [10,13,16,19,25],[22,24,25],[28,27,26,25],[25,30,35,40]]
pos=[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],\
    [5,21,22,23,24],[10,25,26,24],[15,27,28,29,24],\
    [24,30,31,20]]

total_score=0
def sol(p,n):
    if n==1:
        if p+move[n]==5:
            #몰라
            pass
