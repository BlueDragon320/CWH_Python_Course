''' 1. Write a program that counts how many vowels are in a given string.'''

text = input("Enter a sentence: ")
sum = 0
vowels = ['a', 'e', 'i', 'o', 'u']
for char in text.lower():
    print(char)
    if(char in vowels):
        sum+=1

print(f"There are {sum} vowels in this sentence")

'''2. Take a user input string and check if it is a palindrome'''

str1 = "BoB"

if(str1==str1[::-1]):
    print("This string is a palindrome")
else:
    print("This is not a palindrome")