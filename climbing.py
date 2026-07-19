n=2
individual=0
pairs=0
for i in range(n):
    if i*n==n:
            individual+=1
    for j in range(n):
        if i+j==n:
            pairs+=1
ways=individual+pairs
print(ways)
