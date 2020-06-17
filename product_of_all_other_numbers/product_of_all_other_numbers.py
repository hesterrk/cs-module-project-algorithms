'''
Input: a List of integers
Returns: a List of integers
'''

# Plan
# Each element in the array gets overwritten by the multiplication of every other element apart from itself
# 2 arrays, one for original and other for product result


def product_of_all_other_numbers(arr):
    # The left and right product arrays will be exactly the same length as our 'array' length
   
    # Left product array (results of all the numbers on the current elements left side multiplied together)
    # traverse this for loop going forwards
    left_product = [0] * len(arr)

    # Right product array (results of all the numbers on the current elements right side multiplied together)
    # traverse this going backwards
    right_product = [0] * len(arr)

    # Final result array: will contain the result of each element's left and right product multiplied together so its elements before and after can be multiplied together
    final_product = [0] * len(arr)

    # Edge cases
    # in left product array, the first element (left most) in 'arr' has nothing to the left of it so we say its product is '1'
    left_product[0] = 1

    # in the right product array, the last element in 'arr' has nothing to its right, so we say the product is '1'
    right_product[len(arr)-1] = 1

    # First loop, over length of'arr' to construct our left_product array (full of 0's for the length of 'arr')
    # we loop over length to create an index for each product
    # start at index 1 as index 0 is already 1 and end at end of length of left_product array
    for i in range(1, len(arr)):
        # for each index in our left_product array we assign the result of the product of multiplying each number left to the current 'i' we are on
        # we say the product at that index (same index as in our 'arr' so we know we are talking about the same element) is the index before it in our 'arr' multiplied by
        # the left_product[i-1] gets the total product up until the current index in the left products array
        # we use 'i -1' because when we start looping over the first element is already got a product result.
        # so the result for index 1 on our left_product array would be the: the first index in 'arr' array multiplied by the result at index 0 in our left_products array (the latter already been set at 1)
        left_product[i] = arr[i - 1] * left_product[i - 1]

    # We want to start the loop at the second to last element as the last element already has its product as '1' as there is nothing to the right of it
        # we specify this as the first parameter
        # second parameter is where we want to stop: -1 is the index as the we loop down that is the first element 
        # third param is how many steps down we want to go when we loop, we want to loop down one step each time
    for i in range(len(arr)-2, -1, -1):
        right_product[i] = arr[i + 1] * right_product[i + 1]
        print(right_product[i], 'rr')

    # Multiply at each index our left_product and right_product arrays results to get the final product of multiplication of the left and right elements to the current element
    for i in range(len(arr)):
        final_product[i] = right_product[i] * left_product[i]

    return final_product


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
           9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
