def get_grade():
    print("Hello")

get_grade()

mark_list = [55, 45, 23, 85, 74, 90]

for mark in mark_list:
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
                    if mark > 75 and mark <= 100:
                        print("A")
                    else:
                        print("Invalid Mark") 
