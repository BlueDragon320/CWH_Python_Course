# 1. Print numbers from 1 to 10 using a while loop.

i = 1
while i < 11:
    print(i)
    i+=1

# 2. Write a program that keeps asking the user to enter a password until they enter the correct one.

password = 234
user_password = ""
while user_password != password:
    user_password = input("Enter the password: ")
    
    if user_password == password:
        print("Access Granted!")
    else:
        print("Incorrect. Try again.")
        
# 3. Use a while loop to reverse a given number (e.g., 123 → 321).

number = 1234
reversed_num = 0

while number > 0:
    last_digit = number % 10
    reversed_num = (reversed_num * 10) + last_digit
    number = number // 10

print(reversed_num)