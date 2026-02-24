'''2. Read, Write and Append Files
        1. Write a program that writes three lines of text to a file tasks.txt
        2. Open tasks.txt in append mode and add a new line "Task Completed!".
        3. Read the file and print all lines as list using readlines(). '''

f = open("PRACTICE_SET_08/tasks.txt", "w")
content = "Line number 01\nLine numer 02\nline nunmber 03"
f.write(content)
f.close()


f = open("PRACTICE_SET_08/tasks.txt", "a")
content = "\nTask Completed!"
f.write(content)
f.close()

f = open("PRACTICE_SET_08/tasks.txt", "rt")
for lines in f:
    print(lines)

f.close()
    