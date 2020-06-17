'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

# k is a constant integer
# find length of array to determine how many windows 
# First window: index 0 --> i + k (if k is three, k will be index 3 in nums array)
# Second window: index k + 1 --> index k + 4

# Two for loops, one outer and one inner 
    # Outer starts at index 0 of nums array
    # Inner starts at same place and goes up until i + k first time
    # Inner prints max of the first window 
    # Inner carries onto to the next 'k' elements and prints max of those until end of array
    # Overall inner loop runs for 'k' iterations, so it increases by k each loop!
# Another array to store the max of each 'k' window result 


def sliding_window_max(nums, k):
    # Your code here

    pass


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
