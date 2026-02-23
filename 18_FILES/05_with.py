f = open("18_FILES/demo_01.txt")
content = f.read()
print(content)
f.close()



with open("18_FILES/demo_01.txt", "r") as f:
    content = f.read()
    print(content)