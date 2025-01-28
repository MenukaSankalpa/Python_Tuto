def get_grade(mark, subject="Uknown"):
    print("Subject = ", subject)
    if mark >= 0 and mark < 35:
        print("W")
    else:
        if mark >= 35 and mark < 55:
            print("S")
        else:
            if mark >= 55 and mark < 65:
                print("C")
            else:
                if mark >= 65 and mark < 75:
                    print("B")
                else:
                    if mark >= 75 and mark <= 100:
                        print("A")
                    else:
                        print("Invalid Mark") 
                        
                        
get_grade(75, "Sinhala")
get_grade(45, "Maths")                        