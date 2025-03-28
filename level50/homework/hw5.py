# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

def move_zeros(arr):
    result = []
    zero_count = 0
    
    for num in arr:
        if num != 0:
            result.append(num)
        else:
            zero_count = zero_count + 1

    for i in range(zero_count):
        result.append(0)
    
    return result