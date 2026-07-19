s='hello'
list=[]
for i in range(len(s)-1,-1,-1):
    list.append(s[i])
news=''.join(list)
print(news)
