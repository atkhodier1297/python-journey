numbers = [5, 7, 13, 9, 11, 13]
numbers.append(15)
print(numbers)

numbers.insert(0, 3)
print(numbers)

numbers.remove(5)
print(numbers)

# numbers.clear()

numbers.pop()
print(numbers)

print(numbers.index(11))

print(500 in numbers)
# Checks for the object in the list.

print(numbers.count(13))

numbers.sort()
numbers.reverse()
print(numbers)

numbers2 = numbers.copy()
print(numbers2)

numbs = [2, 2, 2, 6, 6, 600, 300, 9, 9]
uniques = []

for num in numbs:
    if num not in uniques:
        uniques.append(num)
print(uniques)

