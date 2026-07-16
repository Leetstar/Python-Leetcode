
a = [11, 7, 1, 13, 21, 3, 7, 3]
b= [11, 3, 7, 1, 7]

def subset(a,b):
    for j in b:
        if j not in a:
            return False
    return True
if subset(a,b):
    print('True')
else:
    print('False')
