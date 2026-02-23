f = open("18_FILES/hi.txt", "rt") # To read text files use "rt" for binary files "rb"

content = f.read()

print(content)
f.close()