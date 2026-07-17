def Sorting(arr,l):
    for i in range(l):
        for j in range(i,l-1):
            if arr[i]>=arr[j+1] :
                arr[i],arr[j+1]=arr[j+1],arr[i]
    return arr 

arr=[3,3,0, 0,5,5,4,4, 2, 1, 1]
l=len(arr)
d=Sorting(arr,l)
print(d)
