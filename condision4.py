height = 175

#1 method
'''if height > 150:
    print("Security")
else:
    print("Labor")'''     
    
#2 method
#if height > 150:
#    job = "Security"
#else:
#    job = "Labor"
#print(job)  

#3 method
height = 175
job = "Security" if height > 150 else "Labor"    
print(job)

#ternary 
msg = "Your job is" + "Security" if height > 150 else "Labor"
print(msg)