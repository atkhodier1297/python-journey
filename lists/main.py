names = ['Adam', 'John', 'Mary', 'Kevin']

print(names)
print(names[0])
print(names[2:])

# Above code does not modify original list.

names[0] = 'Jon'

print(names)

# Above code modified John to Jon.

numbers = [3, 6, 9, 12, 15, 18, 21]
max = numbers[0]

for number in numbers:
    if number > max:
        max = number
print(max)

# Set max to first number then compare it to every index including itself.

