
cities=int(input())
distance = list(map(int,input().split()))
oils= list(map(int,input().split()))

last=oils[0]
price=oils[0]*distance[0]
for i in range(1,len(distance)):
    if oils[i] > last:
        price+=last*distance[i]
    else:
        last=oils[i]
        price+=oils[i]*distance[i]
print(price)
