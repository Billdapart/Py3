# Write a Python program to convert temperatures to and from celsius, fahrenheit. Go to the editor
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
# Expected Output :
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius


#present interface and define unit of measurement variables

tempnum=input("Enter the temperature in (C) for Celsuis, or (F) for Fahrenheit.")

if tempnum == "":
    print("invalid, please input value")
    tempnum =input("Please re-enter the temperature in whole numbers")

unit=input("What unit of measurement? Please enter C for Celsius or F for Fahrenheit.")

#define function to get numbers out of string and output to new variable

num = int(tempnum)

#Convert the temperature for all units using if statement

if unit == "C":
  Temp = (num * 9/5) + 32
  print(str(num) + " degrees Celsius is " + str(Temp) + " Fahreneit!")

elif unit == "F":
    Temp = (num - 32) * 5/9
    print(str(num) + " degrees Fahrenheit is " + str(Temp) + " Celsius!")

else:
  print("Invalid syntax, please restart and enter either 'C' or 'F' in caps")
