x = [12, 23, 567, 123, 88]

total = 0
max = 0
min = 0

for i in x:
    if min > i:
        min = i

for i in x:
    if max < i:
        max = i
        
for i in x:
    total += i
    
print("Total", total)
print("Avg", total/len(x))
print("Max", max) 
print("Min", min)   