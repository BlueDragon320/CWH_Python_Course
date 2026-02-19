def sum(a,b):
    # a and b are local variables
    c = a + b
    z = 1
    print(z)
    return c

def greet():
    z = 32 # Local varibale
    print("Hello")

z = 8 # z is a global variable
print(sum(4,6))
print(z)
