def greet_user(name):
    print(f'hi {name}!')

print("start")
greet_user("Adam")
greet_user("John")

# Define functions first before calling them.
# Parameter would be the name in the original function...an argument would be what we pass in the function when we call it...such as Adam.

def hello_user(first_name, last_name):
    print(f'Hello {first_name} {last_name}!')

hello_user("Adam", "Khodier")

# Multiple arguments
# Most of the time we use positional args, but you can use keyword args when it's not so apparent.
# Helps improve code read ability.

calc_cost(total = 50, shipping = 10, discount = 0.1)

# If the above function was real it is clearly apparent what the args passed into the function mean.
# If you mix pos and key word args make sure positional args go first when you call your function.