S=input()

for s in S:
    if ord(s)<ord("A") or ord(s)>ord("z"):
        print(s,end='')
    elif ord(s)>ord("Z"):
        if ord(s)+13>ord("z"):
            print(chr(ord("a")+(ord(s)+13)-ord("z")-1),end='')
        else:
            print(chr(ord(s)+13),end='')
    elif ord(s)<ord("a"):
        if ord(s)+13>ord("Z"):
            print(chr(ord("A")+(ord(s)+13)-ord("Z")-1),end='')
        else:
            print(chr(ord(s)+13),end='')
