def star(n):
    star_li =[]
    if n==3:
        star_li=[['*','*','*'],
                 ['*',' ','*'],
                 ['*','*','*']]
        blank=[[" "," ",' '],
              [' ',' ',' '],
              [' ',' ',' ']]
        return (star_li,blank)
    else:
        a ,b= star(n//3)
        star_li =[[a,a,a],
                  [a,b,a],
                  [a,a,a]]
        blank=[[b,b,b],
                [b,b,b],
                [b,b,b]]
        return star_li,blank

n = int(input())
q=1
for i in range(1,9):
    if 3**i==n:
        q=i

b,c = star(9)
'''
for m in range(3):
    for j in range(3):
        for k in range(3):
            for i in range(3):
                print(b[m][k][j][i],end="")
        print()
'''
