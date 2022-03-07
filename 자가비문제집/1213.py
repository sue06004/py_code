from collections import Counter
name=input()

counter=Counter(name)
odd=0
odd_s=""
for s in counter:
    if counter[s]%2!=0:
        odd+=1
        odd_s=s
if odd>1:
    print("I'm Sorry Hansoo")
else:
    li=sorted(counter.items())
    left,right="",""
    for i in range(len(li)):
        left+=li[i][0]*(li[i][1]//2)
        right+=li[i][0]*(li[i][1]//2)
    print(left+odd_s+right[::-1])

'''
문자별 개수를 dictionary를 이용해 저장한다.
문자의 개수가 홀수개인 문자의 수가 2개 이상이면
팰린드롬을 만족할 수 없다.
만약 1개이하라면 그 문자를 임의의 변수에 저장해둔다
그리고 dictionary를 items()메소드를 이용해서 [key,value]
인 리스트를 만들고 key값을 key로 하여 정렬한다
그리고 left,right로 나눠서 리스트 처음부터
문자를 개수의 1/2만큼 넣어준다.
그리고 left와 right역순 사이에 아까 임의의변수에 저장해둔
문자의개수가 홀수개인 문자를 넣어준다.

'''