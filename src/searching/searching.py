def linear_search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found

linear_search([-2, 7, 3, -9, 5, 1, 0, 4, -6], 0)

# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    # get the middle index of the array
    high = len(arr) - 1
    while low <= high:
        # search starting at the middle of the array
        middle_index = int((low + high) / 2)
        guess = arr[middle_index]
        if guess == target:
            return middle_index
        if guess > target:
            high = middle_index - 1
        else:
            low = middle_index + 1            
    return -1

binary_search([-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9], 9)
