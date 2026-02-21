'''1. Create a dictionary student = {"name": "John", "age": 20, "grade":"A"} and:
    1. print the vlaue of "name"
    2. chnage "grade" to "A+"
    3. Add a new key "city" with value "delhi"'''
    
    
student = {"name": "John", "age": 20, "grade":"A"}
s1 = student["name"]

print(s1)
student["grade"]="A+"
print(student)





'''2. Create a dictionary of three friends and their phone numbers. Use:
    1.keys() to get all names
    2.values() to get all numbers
    3.items() to loop over key-value pairs and print them'''
    
frands = {"name":"raju", "phone":9942873647, "name":"chotabheem", "phone":9837423487, "name":"chutki","phone":4927038434}


print(frands.keys())
print(frands.values())
print(frands.items())