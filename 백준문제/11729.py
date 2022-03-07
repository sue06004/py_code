def hanoi(n,from_pos,aux_pos,to_pos)->int:
    if n==1:
        print(from_pos,to_pos)
        return
    hanoi(n-1,from_pos,aux_pos,to_pos)
    print(from_pos,to_pos)
    hanoi(1,to_pos,aux_pos,from_pos)


