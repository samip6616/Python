
# Program to reverse a string using a for loop

# Take input from the user
text = input("Enter a string: ")

# Initialize an empty string to store the reversed result
reversed_text = ""

# Loop through the string in reverse order
for char in text:
    reversed_text = char + reversed_text   # Add each character at the beginning

# Print the reversed string
print("Reversed string:", reversed_text)