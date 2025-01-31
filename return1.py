def get_grade(marks, subject=None):
    
    #if not subject:
    #    print("Health is not in list.")
    #    return
    
    if marks < 0 or marks > 100:
        grade = None
    elif marks < 35:
        grade = "W"
    elif marks < 55:
        grade = "S"
    elif marks < 65:
        grade = "B"
    elif marks < 75:
        grade = "B"
    else:
        grade = "A"
    
    print("Hello")    
        
    return subject, grade    
    
grade = get_grade(75)

print(type(grade))

if grade:
    print("Garde = ", grade)
else:
    print("Something went wrong!")        
        