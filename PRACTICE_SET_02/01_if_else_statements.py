# 1. Write a program that asks the user for a number and prints whether it is positive, negative, or zero.

num = int(input("Enter a number: "))

if(num > 0):
    print("The number is positive\n")
elif (num < 0):
    print("The number is negative\n")
else:
    print("The number is 0\n")
    
# 2. Create a program that checks if a person is eligible to vote (age >= 18).

age = int(input("Enter the age: "))

if(age > 18):
    print("You are eligible for voting\n")
else: 
    print("You are not eligible to vote\n")
    
# 3. Write a program that takes a number from the user and prints “Even” if it is even, otherwise “Odd”.

num = int(input("Enter a number : "))

if((num%2)==0):
    print("Number is even\n")
else:
    print("Number is odd\n")