n=int(input())
sung = [input() for _ in range(n)]
di={}
result=[]
for i in range(n):
    if sung[i][0] in di:
        di[sung[i][0]]+=1
    else:
        di[sung[i][0]]=1
    if di[sung[i][0]]>=5 and sung[i][0] not in result:
        result.append(sung[i][0])
        
result.sort()
if not result:
    print("PREDAJA")
else:
    print(''.join(result))