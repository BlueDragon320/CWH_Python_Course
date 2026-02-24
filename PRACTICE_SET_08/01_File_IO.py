'''1. File I/O Basics
        1. Create a text file notes.txt using Python and write "Learning Python is fun!" into it.
        2. Open notes.txt, read its content, and print it to the console.'''


# 1. 
# opern = open("PRACTICE_SET_08/notes.txt", "w")
# content = "Learning Python is fun!"
# opern.write(content)
# opern.close()

# 2.
f = open("PRACTICE_SET_08/notes.txt", "rt")
content = f.read()
print(content)
f.close()