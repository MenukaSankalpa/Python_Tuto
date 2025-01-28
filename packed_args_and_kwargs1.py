def my_form(**parms):
    if 'name' not in parms:
        print("Error")
    else:
        print("Hello", parms['name'])    
    print(parms)
    
    
my_form(name="menuka", height=154, city="Pandura")
my_form(name="menu", height=154, city="")    