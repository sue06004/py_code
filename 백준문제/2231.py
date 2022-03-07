n = int(input())

i=n-100
while i<n:
    if sum(list(map(int,(str(i)))))+i == n:
        break
    else:
        i+=1

print(i) if i<n else print(0)