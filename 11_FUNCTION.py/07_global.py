def sum(a,b):
    print("Hey I am summing")
    c = a + b
    global z # Please modify global z
    z = 0 # This will refer to global z and create a local varible
    return c

print(sum(3, 12))