print("****************************************************")
print("        Welcome to WISystems calculator             ")
print("****************************************************")
print("")
print("This calculator will help you to calculate addition, subtraction, multiplication and division")
print("")

Num1 = int(input("Enter the first number: "))
Variable = input("Enter the operation you want to perform: ")
Num2 = int(input("Enter the second number: "))
if Variable == "+":
    print("The result is: ", Num1 + Num2)
elif Variable == "-":
    print("The result is: ", Num1 - Num2)
elif Variable == "*":
    print("The result is: ", Num1 * Num2)
elif Variable == "/":
    print("The result is: ", Num1 / Num2)
else:
    print("Invalid operation")
print("")
print("****************************************************")
print("        Thank you for using WISystems calculator    ")
print("****************************************************")