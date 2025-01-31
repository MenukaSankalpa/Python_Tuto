def get_grade(marks, subject=None):
    
    if not subject:
        print("Health is not in list.")
        return
    
    if marks < 0 or marks > 100:
        grade = None
    elif marks < 35:
        return "W"
    elif marks < 55:
        return "S"
    elif marks < 65:
        return "B"
    elif marks < 75:
        return "B"
    else:
        return "A"
    
grade = get_grade(-75)
if grade:
    print("Garde = ", grade)
else:
    print("Something went wrong!")        
        