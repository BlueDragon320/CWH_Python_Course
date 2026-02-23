import os

a = os.listdir("dir") # as the name suggest this shows every file in directory
print(a)

print(os.getcwd()) # This shows cwd that means current working directory
 
print(os.path.exists("dir")) #if exists True else False

# os.remove("sample.txt")
# This will remove the file 

# os.rmdir("dir")
# This will remove the directories