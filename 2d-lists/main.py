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

# 2D List with people's information
people = [
    ["Alice", 25, "Female", "alice@example.com"],
    ["Bob", 30, "Male", "bob@example.com"],
    ["Charlie", 22, "Non-binary", "charlie@example.com"]
]

# Iterate over the data rows
for person in people:
    print(f"{person[0]:<10} {person[1]:<5} {person[2]:<10} {person[3]:<20}")
