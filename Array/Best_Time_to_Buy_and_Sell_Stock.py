nums = [7,6,4,3,1]
diff=0
maxdifference=0
for i in range(len(nums)):
    for j in range(len(nums)):
        if j>i:
            diff=nums[j]-nums[i]
        if diff>maxdifference:
            maxdifference=diff

print(maxdifference)
