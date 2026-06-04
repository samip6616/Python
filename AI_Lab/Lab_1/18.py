# Program to check if a string is a palindrome

# Take input from the user
text = input("Enter a string: ")

# Reverse the string using a for loop
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text

# Check if original and reversed strings are the same
if text == reversed_text:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")