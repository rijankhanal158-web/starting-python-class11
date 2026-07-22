#Simple Fahrenheit to Celsius or Celaius to Fahrenheit Calculator

temp=float(input("Enter temperature: "))
unit=input("Enter the unit of temperature (Fahrenheit/Celsius:")

#lets using the conditional terms

if unit=="c":
    temp=(temp*9)/5+32
    print(f"The temperature in Fahrenheit is: {temp} ")
    
elif unit=="f":
    temp=(temp-32)*5/9
    print(f"The temperature in Celsius is:{temp}")
    
else:
    print("Error found , try again!")
    
#Completed Temperature Calculator
    