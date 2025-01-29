# In coding, a palindrome is a string, number, or sequence that reads the same forward and backward.
# Strings: "racecar", "madam", "level"
# Nums: 121, 1331, 12321

# We want to take our input, then reverse it, then see if it's equal to the original input.
# All negative inputs output False.


def is_palindrome(s):
    length = len(s)
    for i in range(length // 2):  # Only loop through half the string
        if s[i] != s[length - i - 1]:  # Compare characters from both ends
            return False
    return True

print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False


def is_number_palindrome(n):
    original = n  # Store the original number
    reversed_num = 0

    while n > 0:
        digit = n % 10  # Get the last digit
        reversed_num = reversed_num * 10 + digit  # Build the reversed number
        n = n // 10  # Remove the last digit from n

    return original == reversed_num  # Check if the original equals the reversed

print(is_number_palindrome(121))  # True
print(is_number_palindrome(123))  # False
print(is_number_palindrome(12321))  # True


