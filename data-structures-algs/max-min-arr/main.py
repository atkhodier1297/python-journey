def find_max_min(arr):
    max_num = arr[0]
    min_num = arr[0]

    for num in arr:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    return max_num, min_num

numbers = [3, 1, 7, 9, 2]
maximum, minimum = find_max_min(numbers)
print(f"Max: {maximum}, Min: {minimum}")
