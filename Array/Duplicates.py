def dp(arr):
    duplicate=[]
    for element in range(len(arr)-1):
         if arr[element] ==arr[element+1]:
            duplicate.append(arr[element])
            return duplicate
    else:
        return []
      
           
           
arr = [3,1,2]
arr.sort()           
d=dp(arr)
print(d)
