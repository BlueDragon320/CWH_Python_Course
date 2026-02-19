'''1. Write a function full_name(first, last) that takes first name and last name as parameters and returns a single string in the format "First Last".'''

def full_name(f_name, l_name):
    return f_name + " " + l_name

f_name = "Phunsuk"
l_name = "wangdu"
print(full_name(f_name, l_name))


'''2. Write a function calculate_area(length, width=10) that returns the area of a rectangle. Test it by calling the function with:
    1. Both length and width
    2. Only length (use default width)'''
    
    
def calculate_area(length, width=10):
    area = length * width
    print(area)
    
calculate_area(10, 20)
calculate_area(10)