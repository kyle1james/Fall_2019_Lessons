# This problem was asked by Google.
# 
# You are given an array of nonnegative integers. 
# Let's say you start at the beginning of the array and are trying to 
# advance to the end. You can advance at most, the number of steps that 
# you're currently on. Determine whether you can get to the end of the array.
# 
# For example, given the array [1, 3, 1, 2, 0, 1], we can go from indices 
# 0 -> 1 -> 3 -> 5, so return true.
# 
# Given the array [1, 2, 1, 0, 0], we can't reach the end, so return false.

def steps(arr):
    furtherst = 0
    
    for idx, num in enumerate(arr):
        # end case false
        if idx > furtherst:
            break
        # keep track of the absolute possible furthest step we can reach
        furtherst = max(furtherst, num + idx)
    
    return furtherst >= len(arr)-1
    
arr1 = [1, 3, 1, 2, 0, 1]
arr2 = [1, 2, 1, 0, 0]

print(steps(arr1))