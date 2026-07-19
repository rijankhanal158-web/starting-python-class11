#Input operato4s and make a simple Calculator#

operator=input(("Enter operator(+, - ,/): "))
num_1=float(input("Enter firts number:"))
num_2=float(input("Enter second number:"))

if operator=="+":
    result=num_1+num_2
    print(f"Your result is: {result}")
    
elif operator=="-":
    result=num_1-num_2
    print(f"Your result is: {result}")
    
elif operator=="/":
     result=num_1/num_2
     print(f"Your result is: {result}")
     
#A calculator without loops  is ready to use#
     


    