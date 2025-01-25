#0-35= w
#35-55=s
#55-65=c
#65-75=b
#75-100=a

M = 56

if M < 0 or M > 100:
    print ("Invalid")

if M >=0 and M<35:#
    print("W")
elif M>=35 and M<55: #elif M<55
    print("S")
elif M>=55 and M<65: #elif M<65
    print("C")
elif M>=65 and M<75: #elif M<75
    print("B")
elif M>=75 and M<=100: #elif M<=100
    print("A")
#else:
#    print("Invalid Number")                     