arr=[-1, 10, 10, 12, 15]
l=len(arr)
target=2
count=0
for i in range(l):
    for j in range(i+1,l):
        if arr[i]+arr[j]==target:
            count+=1
print(count)
