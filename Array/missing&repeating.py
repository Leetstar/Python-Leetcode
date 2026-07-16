
def mr(arr):
    missing_number=[]
    n=int(input('Enter the number-'))
    for i in range(1,n+1):
        if i not in arr:
            missing_number.append(i)
            return missing_number
        
def rp(arr):
    repeating_number=[]
    arr.sort()
    for j in range(len(arr)-1):
            if arr[j]==arr[j+1]:
                repeating_number.append(arr[j])
                return repeating_number
            
    
arr = [1, 3, 3]   
m=mr(arr)
r=rp(arr)
result=r+m
print(result)
