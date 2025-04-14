# Debug the functions
# Should be easy, begin by looking at the code. Debug the code and the functions should work.

# There are three functions: Multiplication (x) Addition (+) and Reverse (!esreveR)

def multi(lst):
    res = 1 
    for num in lst:
        res *= num 
    return res

def add(lst):
    return sum(lst)

def reverse(st):
    return st[::-1]