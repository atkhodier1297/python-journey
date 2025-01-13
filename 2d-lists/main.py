# Example of a 2D list
matrix = [
    [1, 2, 3],  # Row 1
    [4, 5, 6],  # Row 2
    [7, 8, 9]   # Row 3
]

# Iterating over a 2D list
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()  # Newline after each row