# 1. Print numbers from 1 to 10 using a for loop.

# for i in range (1, 11):
#     print(i)

# 2. Print the multiplication table of a number (entered by user).

# num = int(input("Enter the number: "))
# for i in range (1, 11):
#     print(f"{num} x {i} = ", num * i)
    
# 3. Calculate the sum of all numbers from 1 to 100 using a for loop.

num = 1
for i in range (2, 101):
    num += i
    i+=1
print(num)

# 4. Print the following pattern using a for loop:
#     *
#     **
#     ***
#     ****
#     *****

for i in range (1, 6):
    print("*" * i)
    