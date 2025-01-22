try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("Age can't be 0.")
except ValueError: # This block is only catching exceptions of that type.
    print('Not a number bro.')

# Exit code 0 means success anything other than that means it failed.
# Print error messages using try and except.
# These prevent your program from crashing and direct the user on what went wrong.