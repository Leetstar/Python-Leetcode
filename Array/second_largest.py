
arr = [12, 35, 1, 10, 34, 1]
l=len(arr)
largest=0
second_largest=0
for i in range(l):
    for j in range(l-1):
        if arr[i]>largest:
            largest=arr[i]
        if arr[j+1]>arr[j] and arr[j+1]<largest:
            second_largest=arr[j+1]
print(second_largest)
print(largest)

        
#2,1,4,3,5
#13, 46, 24, 52, 20, 9
