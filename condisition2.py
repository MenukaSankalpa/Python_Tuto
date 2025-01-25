#0-35= w
#35-55=s
#55-65=c
#65-75=b
#75-100=a

mark = 50

if mark >=0 and mark < 35:
    print("W")
else:
    if mark >=35 and mark < 55:
        print("S")
    else:
        if mark >=55 and mark < 65:
            print("C")
        else:
            if mark >=65 and mark < 75:
                print("B")
            else:
                if mark >75 and mark <=100:
                    print("A")
                else:
                    print("Invalid Mark")                
