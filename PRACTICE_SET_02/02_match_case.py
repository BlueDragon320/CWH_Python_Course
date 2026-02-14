# 1. Ask the user to enter a day number (1–7) and print the corresponding day of the week using match case 

num = int(input("Enter a number between 1 to 7: "))
match num:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid number")
        
        
# 2. Write a program using match case that simulates a simple calculator.
# 1. Ask the user for two numbers and an operation (+, -, *, /).
# 2. Perform the operation using match case .

num1 = int(input("Enter number 1: ")) 
num2 = int(input("Enter number 2: ")) 
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
operation = int(input("Enter the operation numbner: "))
match operation:
    case 1:
        print("Addition = ", num1+num2)
    case 2:
        print("Subtraction = ", num1-num2)
    case 3:
        print("Multiplication = ", num1*num2)
    case 4:
        print("Division = ", num1/num2)
    case 5:
        print("Exiting.")
        