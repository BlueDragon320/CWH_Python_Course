'''1. Given text = "Python Programming", do the following:
        1. Print the first 6 characters
        2. Print the last 6 characters
        3. Print every secound character from the string'''

text = "Python Programming"

print(text[0:6])
print(text[-6:])
print(text[0:18:2])


'''2. Reverse the string text using slicing.'''

text = "Python Programming"
print(text[::-1])