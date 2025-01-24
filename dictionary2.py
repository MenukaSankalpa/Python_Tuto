x = {1: 'A', 2: 'B', 3: 'C', 5: 'E'}

#y = x[1]
y = x.get(4 , 'D')
del x[5]
print(x)
print(y)
