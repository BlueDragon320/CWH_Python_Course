'''1. Write a lambda function that adds two numbers and test it.'''

sum = lambda x, y: x + y
print(sum(1, 2))

'''2. Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get their squares.'''

numbers = [1, 2, 3, 4, 5]
squares = map(lambda x: x**2, numbers)

squares_list = list(squares)
print(squares_list)
