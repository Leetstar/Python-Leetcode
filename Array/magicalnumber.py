def magic(arr):
    magical_number=0
    for i in range(len(arr)):
        if arr[i]==i:
            magical_number=i
            return magical_number
    else:
        return -1
        
arr=[-2, -1, 2,3, 4, 6]
m=magic(arr)
print(m)

