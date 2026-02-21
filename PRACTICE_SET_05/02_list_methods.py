'''1. Start with numbers = [5, 2, 9, 1, 7] and do the following:
    1. Sort the list in asccending order.
    2. Append te number 10 to the list.
    3. Remove the number 10 to the list.'''
    
numbers = [5, 2, 9, 1, 7]
print(numbers)
numbers.sort()
print("Ascending Order: ", numbers)
numbers.append(10)
print("Append (10) (join): ", numbers)
numbers.remove(10)
print("Remove (10): ", numbers)

'''2. Create a list names = ["Alice", "Bob", "Charlie"] and use the insert() method to add "David" at index 1.'''

names = ["Alice", "Bob", "Charlie"]
names[1] = "David"
print(names)