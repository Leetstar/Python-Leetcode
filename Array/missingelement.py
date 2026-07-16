def miss(arr):
    missing=0
    n=int(input('Enter the numebr-'))
    for i in range(1,n+1):
        if i not in arr:
            missing=i
            return missing
arr=[1,2,3,5]
missingelement=miss(arr)
print('missing element=',missingelement)
