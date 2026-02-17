''' 1. Given sentence = "Coding in Python is fun", replace "fun" with "awesome and print it"
    2. Find the index of the word "Python" in sentence.
    3. Convert the entire sentence to uppercase and print it.
'''

text = "Coding in Python is fun"

edit_text1 = text.replace("fun", "awesome")
print(edit_text1)

print(text.index("Python"))

edit_text2 = text.upper()
print(edit_text2)