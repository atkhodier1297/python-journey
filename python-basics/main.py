# Printing in Python.

print('Hello World, I am Adam Khodier')
print('o----')
print(' ||||')

print('*' * 10)
# Python interpreter evaluating our expression on line 4 creates 10 asterisks.

# Python variables. Integers/Floats/Boolean just like JS

price = 10
price = 20
rating = 4.9
is_published = True
print(price)
print(is_published)

name = input('What is your name? ')
fav_color = input('What is your favorite color? ')
print(name + ' likes ' + fav_color)

birth_year = input('Birth year: ')
print(type(birth_year))
age = 2024 - int(birth_year)
print(type(age))
print(age)
# Input function in Py is always a string so if you expect an integer value make sure to convert it to a integer or float.

print("Python's") 
# Use "" to define certain strings in Py to avoid errors.

message = '''
Welcome! 😊 How can I assist you today? 
Whether you're diving into coding challenges, exploring product management, 
or anything else, I’m here to help!
'''
print(message)
# Py string indexes start at 0 like JS

course = 'Python for beginners'
print(course[0])
print(course[0:5])

first = 'Adam'
last = 'Khodier'
msg = f'I think {first} {last} is a coder!'
# Formatted strings are easier to visualize compared to string concatenation.
print(msg)