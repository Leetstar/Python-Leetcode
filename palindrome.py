n=153
s=0
p=n
while p>0:
    r=p%10
    p=p//10
    s+=r**3
print(s)
