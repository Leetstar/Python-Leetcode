s='malayalam'
list=[]
for i in range(len(s)-1,-1,-1):
    list.append(s[i])
news=''.join(list)
if news==s:
    print('is a palindrome')
else:
    print('Not a palindrome')
