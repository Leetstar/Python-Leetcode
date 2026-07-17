def zeroes(arr):
   for i in range(len(arr)):
      for j in range(i,len(arr)-1):
          if arr[j]==0:
            arr[j],arr[j+1]=arr[j+1],arr[j]
       
   print(arr)

arr=[1,0,2,0,3]


zeroes(arr)
