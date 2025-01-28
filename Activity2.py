d = {
    "Name": "Menuka",
    "Age": 21,
    "Color": "black",
    "Pet": "pati" 
}

for name, height in d.items():
    print(type(name))
    print(name, height)
    
#for name in d:
#    height = d[name]
#    print(name, height)

for i, x in enumerate(d.items()):
    name, height = x
    print(name , height)