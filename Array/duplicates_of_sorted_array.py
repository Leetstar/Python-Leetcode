arr=[1,1,1,2,2,3,3,3,3,4,4]
n=int(input('Enter the element'))
l=len(arr)
duplicate=[]
for i in range(n):
    for j in range(1,l):
        if arr[i]!=arr[j]:
            arr[j]=arr[i]
        result=i+1
    
print(result)
