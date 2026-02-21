'''1. Create a list fruits = ["apple", "banana", "cherry"]
    1. Print the first fruit.
    2. Replace "banana" with "orange".
    3. Print the length of the list'''
    

fruits = ["apple", "banana", "cherry"]
fruits[1] = ["orange"]

print(fruits)

fr1 = len(fruits)
print(fr1)



'''2. Creat a list of numbers from 1 to 10
        1.Print the first 3 numbers using slicing.
        2.Print the last 3 numbers using slicing.'''
        
        
list1 = [i for i in range(1, 11)]
print(list1)

print(list1[0:3])
print(list1[-3:])