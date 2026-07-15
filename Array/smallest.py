
arr=[4,3,5,1]
l=len(arr)
smallest=arr[0]
for i in range(l-1):
    if arr[i+1]<smallest:
        smallest=arr[i+1]
print(smallest)
