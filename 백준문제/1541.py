
a = input()
li=[]
start=0
for i in range(len(a)):
    if a[i]=="+" or a[i]=="-":
        li.append(int(a[start:i]))
        li.append(a[i])
        start=i+1
    elif i==len(a)-1:
        li.append(int(a[start:]))

result=[]
i=0
while i < len(li):
    if li[i]=="+":
        result[-1]+=li[i+1]
        i+=1
    elif li[i]=="-":
        result.append(0)

    else:
        result.append(li[i])    
    i+=1

i=1
b=result[0]
for i in result[1:]:
    b-=i
print(b)
