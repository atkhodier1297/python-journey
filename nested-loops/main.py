for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")

numbers = [5, 2, 5, 2, 2]

for x_count in numbers:
    print ('x' * x_count)
# In Py remember we can multiply strings by numbers but solve it with an interloop.

for o_count in numbers:
    output = ''
    for count in range(o_count):
        output += 'o'
    print(output)