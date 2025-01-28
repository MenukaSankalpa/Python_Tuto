x = [12, 23, 567, 123, 88]

count = 0
total = 0
min = max = x[0]

while count < len(x):
    item = x[count]
    
    if item > max:
        max = item
    
    if item < min:
        min = item    
    
    total += item
    
    count += 1
    
print("Total", total)
print("Avg", total/len(x)) 
print("Max", max)
print("Min", min)   