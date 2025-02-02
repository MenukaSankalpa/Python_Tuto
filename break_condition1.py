x = [12, 23, 567, 123, 8]

count = 0

'''for i in x: 
    if i >= 100:
        break
    print(i)'''
    
for i in x:
    if i % 2 == 0:
        continue
    
    print(i)
    print(i ** 2)
        
    
while count == len(x) - 1:
    print("Index", count)
    
    i = x[count]
    
    if i % 2 == 10:
        count += 1
        continue
    
    print(i)
    print(I ** 2)
    count += 1  