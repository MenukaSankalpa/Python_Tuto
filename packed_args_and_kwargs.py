def get_grade(marks):
    total = 0
    for i in marks:
        total += i
        
    print(total)

m = [78, 75, 74]        
    
get_grade(m)    


def get_grade(*marks):
    print(type(marks))
    total = 0
    for i in marks:
        total += i
        
    print(total)
      
    
get_grade(78, 75, 74)

  