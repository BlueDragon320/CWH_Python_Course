'''3. OS and Shutil Modules
    1. Use th os module to:
        1. Print the current working directory
        2. list all files and folders in the current direcotry
        3. Create a new folder my_folder
    2. Use the shutil module to:
        1. Copy a file from one folder to another
        2. Move a file to a new folder
        3. Delete a file(careful:irreversible!)
    '''
    
# import os
# current_directory = os.getcwd()
# list_files  = os.listdir()
# create_directory = os.mkdir("PRACTICE_SET_08/my_folder")
# print(current_directory)
# print(list_files)


import shutil
# shutil.copy("PRACTICE_SET_08/notes.txt", "PRACTICE_SET_08/my_folder/notes.txt")
# shutil.move("PRACTICE_SET_08/notes.txt", "PRACTICE_SET_08/my_folder/notex.txt")
shutil.rmtree("PRACTICE_SET_08/my_folder")