import sys
input = sys.stdin.readline

sudoku=[list(map(int,input().split())) for _ in range(9)]

def setSudoku(sudoku):
    