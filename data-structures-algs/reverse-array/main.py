def reverse_array_in_place(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

arr = [1, 2, 3, 4, 5]
reverse_array_in_place(arr)
print(arr)  # Output: [5, 4, 3, 2, 1]


arr = [1, 2, 3, 4, 5]
arr.reverse()
print(arr)  # Output: [5, 4, 3, 2, 1]
