# Simple Weight Calculator#

weight=float(input("Enter your weight: "))
unit=input("Enter your unit (k/l) : ")

#Conditional #

if unit=="k":
    weight=weight * 2.205
    unit="Lbs"
    print(f"Your weight is: {round(weight,2)}{unit}")  
    
elif unit=="l":
    weight=weight / 2.205
    unit="Kgs"
    print(f"Your weight is: {round(weight,2)}{unit}")
    
else:
    print(f"{unit} is not vaild ,Try again!")
    
# Done #