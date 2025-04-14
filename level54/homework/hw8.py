# Preface
# A collatz sequence, starting with a positive integern, is found by repeatedly applying the following function to n until n == 1 :

# f (n)={n/2, if n in even 3 n + 1 , if m is odd
# f(n)={ 
# n/2, if n is even
# 3n+1, if n is odd

def collatz(n):
    res = ""
    while n > 1:
        if n % 2 != 0:
            res += str(n) + "->"
            n = n*3 +1
        else:
            res += str(n) + "->"
            n = n //2
    return res + "1"