'''
0 1 1 2 3 5 8 13
0 1 2 3 4 5 6........

fib(0) = 0
fin(1) = 1
fin(2) = fib(0) + fib(1)
fib(3) = fib(1) + fib(2)
'''

def fib(n):
    # Base case of recursion
    if(n==0 or n==1):
        return n
    
    return fib(n-2) + fib(n-1)


print(fib(5))