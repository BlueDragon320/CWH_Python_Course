try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    print("Choose Operation to perform from the options given below: \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Remainder\n")
    o = int(input("Enter Operation: "))
    match o:
        case 1:
            print(f"Addition of {a} + {b} = {a+b}")
        case 2:
            print(f"Subtraction of {a} - {b} = {a-b}")
        case 3:
            print(f"Multiplication of {a} x {b} = {a*b}")
        case 4: 
            print(f"Division of {a} / {b} = {a/b}")
        case 5:
            print(f"Remainder of {a} % {b} = {a%b}")
        case default:
            print("Error")
            
        
except Exception as e:
    print("Enter a valid value as a and b")