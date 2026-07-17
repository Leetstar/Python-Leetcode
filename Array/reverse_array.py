def reverse_array(arr):
    new_array=[]
    for i in range(len(arr)-1,-1,-1):
        new_array.append(arr[i])
    return new_array

arr = [1]
a=reverse_array(arr)
print(a)
