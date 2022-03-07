import sys
input = sys.stdin.readline

n=int(input())
board_=[list(map(int,input().split())) for _ in range(n)]
mx=0
def left_(board):
    global mx
    for i in range(n):
        left,right=0,1
        while right < n:
            if board[i][left]==board[i][right] and board[i][left]!=0:
                board[i][left]*=2
                board[i][right]=0
                left+=1
                right=left+1
            elif board[i][right]!=0:
                if board[i][left]==0:
                    board[i][left]=board[i][right]
                    board[i][right]=0
                    right+=1
                elif right-left>1:
                    board[i][left+1]=board[i][right]
                    board[i][right]=0
                    left+=1
                    right+=1
                else:
                    left+=1
                    right+=1
            else:
                right+=1
        mx=max([mx]+board[i])
    return board
def right_(board):
    global mx
    for i in range(n):
        left,right=n-2,n-1
        while left >=0:
            if board[i][left]==board[i][right] and board[i][right]!=0:
                board[i][right]*=2
                board[i][left]=0
                right-=1
                left=right-1
            elif board[i][left]!=0:
                if board[i][right]==0:
                    board[i][right]=board[i][left]
                    board[i][left]=0
                    left-=1
                elif right-left>1:
                    board[i][right-1]=board[i][left]
                    board[i][left]=0
                    right-=1
                    left=right-1
                else:
                    right-=1
                    left=right-1
            else:
                left-=1
        mx=max([mx]+board[i])
    return board
def up_(board):
    global mx
    for i in range(n):
        up,down=0,1
        while down<n:
            if board[up][i]==board[down][i] and board[up][i]!=0:
                board[up][i]*=2
                board[down][i]=0
                up+=1
                down=up+1
            elif board[down][i]!=0:
                if board[up][i]==0:
                    board[up][i]=board[down][i]
                    board[down][i]=0
                    down+=1
                elif down-up>1:
                    board[up+1][i]=board[down][i]
                    board[down][i]=0
                    up+=1
                    down+=1
                else:
                    up+=1
                    down+=1
            else:
                down+=1
    return board
def down_(board):
    global mx
    for i in range(n):
        up,down=n-2,n-1
        while up>=0:
            if board[up][i]==board[down][i] and board[down][i]!=0:
                board[down][i]*=2
                board[up][i]=0
                down-=1
                up=down-1
            elif board[up][i]!=0:
                if board[down][i]==0:
                    board[down][i]=board[up][i]
                    board[up][i]=0
                    up-=1
                elif down-up>1:
                    board[down-1][i]=board[up][i]
                    board[up][i]=0
                    down-=1
                    up-=1
                else:
                    down-=1
                    up-=1
            else:
                up-=1
    for i in range(n):
        for j in range(n):
            mx=max(mx,board[i][j])
    return board
def dfs(board,a):
    if a==5:
        return
    for i in range(4):
        tmp=[]
        for k in range(n):
            tmp.append(board[k][:])
        if i==0:
            dfs(left_(tmp),a+1)
        elif i==1:
            dfs(right_(tmp),a+1)
        elif i==2:
            dfs(up_(tmp),a+1)
        else:
            dfs(down_(tmp),a+1)
dfs(board_,0)
print(mx)
