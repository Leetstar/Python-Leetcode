arr=[1, 1,1,2,2,2]
l=len(arr)
count=0
maxsum=0
for i in range(l):
    for j in range(i+1,l):
        sum=arr[i]+arr[j]
        if  sum>maxsum:
            maxsum=sum
            count=1
        elif sum==maxsum:
            count+=1
print(count)
