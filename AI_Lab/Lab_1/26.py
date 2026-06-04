# Function to reverse a string using a loop
def reverse_string(text):
    reversed_text = ""  # Initialize empty string

    # Loop through each character
    for char in text:
        reversed_text = char + reversed_text  # Add character at the beginning

    return reversed_text


# Take input from the user
string = input("Enter a string: ")

# Call the function and print the result
result = reverse_string(string)
print("Reversed string:", result)