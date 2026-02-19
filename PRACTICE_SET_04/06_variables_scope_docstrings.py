'''1. Write a function increment() that has a local varibale counter initialized to 0 and increments it by 1 each time it is called. Observer whether the value persists across functino calls.'''


def increment():
    counter = 0
    counter+=1
    print(counter)
    
    
increment()
increment()
increment()

'''2. Write a function
multiply(a, b) that has a proper docstring explaining what
it does. Then use
help(multiply) to display the docstring.'''

