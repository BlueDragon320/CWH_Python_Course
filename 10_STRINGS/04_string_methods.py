name = "ChotaBheem"

a = len(name)
print(a)

print(name.upper()) # CHOTABHEEM
# Original value is not changed
print(name.lower()) # chotabheem
print(name.capitalize()) # Chotabheem


# refer notes for better understanding


# print(variable_name.strip()) removes empty spaces

text = "Python is a programming language"
print(text.find("lang")) # 24th position that is L's position
print(text.replace("a", "an")) # replace a with an all the occurances



print("\n")


text = "Apple, Blueberry, Cherry, Dragonfruit"
print(",".join(["Apple, Blueberry, Cherry, Dragonfruit"]))
print(text.split(","))

print(text, "\n")


mane = "python123"
print(mane.isalpha()) #True if mane is only alphabets else False
print(mane.isdigit()) # True if all digits else False
print(mane.isalnum()) # True if it has both alphabets and numbers else false
print(mane.isspace()) # True if it has all space 