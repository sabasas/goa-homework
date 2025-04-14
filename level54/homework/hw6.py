# Your task is to write function factorial.

def factorial(n):
    factorial=1
    if n==0:
        return 1
    else:
        for x in range (n,1,-1):
            factorial*=x
        return factorial