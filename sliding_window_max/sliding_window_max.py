'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

# k is a constant integer
# We determine how many sub-lists (windows)
# First window: index 0 --> i + k (if k is three, k will be index 3 in nums array)
# Second window: index k + 1 --> index k + 4

# Have a 'max' array to store the max of each 'k' window result and then for each item in max array we can call max() function on it
# We can have one loop which runs across each of the sub-lists in the length of the nums array
# In this loop we can select the current index to the end of the sub-array using list slicing
# the start of each sub-array will be the current index of our loop (i)
#  for each sub-list we select the current index as start of slicing and the current index plus k (gets us to the last element in our sub-list) as the end of the slicing
# After we do this, for each sub-list, we assign each index in our new 'max' array to the value of the maximum of each sub-array using the max function. Hence each value in our max array will contain the result of each of our sub-list's max value
# Then we return our new max list


def sliding_window_max(nums, k):

    # Set up max array:
    # its length is the same length as our outer for loop (which is the number of sub-lists in the nums array)
    max_of_subs = [0] * (len(nums) - k + 1)


# Run our outer loop, have to specify where we want the looping to stop at
    # We want to iterate over the length of the number of sub-lists (number of sub lists is determined by 'k')
    # If k = 3 and length of array is 6 elements
    # Index 0 is the first sub-list which is first loop (first k window): here it grabs element at index 0 to index 2 (slicing happens)
    # Index 1 is the second sub-list which is second loop (second k window): here it grabs element at index 1 to index 3 (slicing happens)
    # Index 2 is the third sub-list which is the third loop (third k window) --> here it grabs element at index 2 to index 4,
    # Index 3 is our fourth sub-list which is the fourth loop (fourth k window) --> here it grabs element at index 3 to index 5
    # we stop it here (we stop it the outer loop at index 3, as index 3 is the start of our last sub-list)
    # We want our outer loop to run from index 0 (where it gets the first element at index 0) to index 3
    # If our list is length of 6 and our k = 3, we want to do length of list - k + 1 because of zero based index, the plus one gets us to the correct index of the last of our sub-lists to loop over. The k is based on our 0 based index so it always needs to be k + 1

    for i in range(len(nums) - k + 1):
        # print(len(nums) - (k + 1))
        sub_list = nums[i:i + k]
        # Now we have the selected all the numbers from each sub-list in the nums array, we assign each index in the max array to the maximum element (gets calculated by the max function) in each sub-list  
        max_of_subs[i] = max(sub_list)

    # return the array to get all the stored max values in sub-lists
    return max_of_subs


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
