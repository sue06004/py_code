
S=input()
li=[0]*26
li2=['a','b','c','d','e','f','g','h','i','j','k','l','m',\
    'n','o','p','q','r','s','t','u','v','w','x','y','z']
for s in S:
    for i in range(26):
        if s==li2[i]:
            li[i]+=1
print(' '.join(map(str,li)))