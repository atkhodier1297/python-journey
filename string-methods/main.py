course = 'Python for beginners.'
print(len(course))
# Gives you length of input.

print(course)
print(course.upper())
# Method to uppercase an input. Makes a new instance of the variable, it does not change the original.
print(course.lower())
# Method to lowercase an input. Makes a new instance of the variable, it does not change the original.

print(course.find('P'))
print(course.find('beginners'))
# Method gives you the index of a certain letter in your string.

print(course.replace('beginners', 'experts'))
# Method to replace a section of your input.

print('Python' in course)
# Method to search your string for certain chars using "in" operator.