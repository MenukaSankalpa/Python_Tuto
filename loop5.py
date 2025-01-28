x = [12, 23, 567, 8, 78,  99, 120, 135]

count = 0

for i in x:
    if i > 100:
        break
    print(i)

for i in x:
    if i % 2 ==0:
        continue
    
    print(i)
    print(i**2)
    
while count == len(x) -1:
    print("index", count)
    
    #if count == len(x) -1:
    #    break
    i = x[count]
    
    if i % 2 == 0:
        count += 1
        continue
    
    print(i)
    
    count += 1   
    