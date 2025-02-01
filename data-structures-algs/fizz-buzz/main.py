def fizzbuzz(n):
    for i in range(1, n + 1):  # Loop from 1 to n
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")  # Multiple of both 3 and 5
        elif i % 3 == 0:
            print("Fizz")  # Multiple of 3
        elif i % 5 == 0:
            print("Buzz")  # Multiple of 5
        else:
            print(i)  # Print the number if not a multiple of 3 or 5

fizzbuzz(15)
