target=int(input('enter the element to be found-'))
arr=[1,2,3,4,5,6]
for i in range(len(arr)):
    if arr[i]==target:
        print(f'element {target} found at {i}th position')
        break
else:
    print('element not found')
