# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        
        # get the current value at the index of list
        value = arr[i]
        
        # to look left subract one from index
        left_index = i - 1
    
        while value < arr[left_index] and left_index >= 0:
            
            
            print(f'\nValues {value} is greater left_index {left_index}')
            # array in current position is swaped with array at previous position
            
            # Why can't we assign to array[i] if it is the same thing
            arr[left_index + 1] = arr[left_index]
            left_index -= 1
            print(arr)
        arr[left_index + 1] = value
    return arr

selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here


    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
