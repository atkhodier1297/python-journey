def two_sum(nums, target):
    h = {}  # Create a hashmap to store numbers and their indices

    # Loop over the list with index and value
    for i, num in enumerate(nums):
        y = target - num  # Calculate the complement

        # Check if the complement exists in the hashmap
        if y in h:
            return [h[y], i]  # Return the indices of the two numbers
        
        # Add the current number and its index to the hashmap
        h[num] = i

# Test the function
nums = [2, 7, 13, 15]  # Example array
target = 9             # Example target
result = two_sum(nums, target)
print(result)          # Expected output: [0, 1]


def two_sum_brute(nums, target):
    # Loop over every pair of numbers
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):  # Ensure i != j
            if nums[i] + nums[j] == target:
                return [i, j]  # Return the indices of the two numbers

# Example usage
nums = [2, 7, 13, 15]
target = 9
result = two_sum_brute(nums, target)
print(result)  # Output: [0, 1]

