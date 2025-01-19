x = [12, 45, 85, 75, 78]
y = [0, 10, 20, 30, 40]

z = x + y
print(z)

x.append(100)

#x.append(4567)
#x.insert(4712)

x.insert(2, 897)
#y = x[3]
#print(y)

x.remove(78)
print(x)
x.pop(1)

#x[4] = 789
print(x)
print(10 in z)
print(789 not in z)