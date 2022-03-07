
def nqueen(sol,n):
    global count
    if len(sol) == n:
        count += 1
        return 
    candidates = list(range(n))
    for i in range(len(sol)):
        if sol[i] in candidates:
            candidates.remove(sol[i])
        distance = len(sol)-i
        if sol[i]-distance in candidates:
            candidates.remove(sol[i]-distance)
        if sol[i]+distance in candidates:
            candidates.remove(sol[i]+distance)
    for i in candidates:
        sol.append(i)
        nqueen(sol,n)
        sol.pop()

n=int(input())
count = 0

for i in range(n):
    nqueen([i],n)
print(count)