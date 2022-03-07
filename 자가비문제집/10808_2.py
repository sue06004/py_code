S=input()
li=[0]*26
for s in S:
    li[ord(s)-ord('a')]+=1
print(' '.join(map(str,li)))
#ord-> 아스키코드로 변환해주는 함수
