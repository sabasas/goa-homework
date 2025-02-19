# You get an array of numbers, return the sum of all of the positives ones.

# Example [1,-4,7,12] => 1 + 7 + 12 = 20

#ef positive_sum(arr):
    # Your code here
    #return 0

def positive_sum(arr):
    total = 0
    for x in arr:
        if x > 0:
            total+= x
    return total    
            