# Program to count vowels in a string

# Take input from the user
text = input("Enter a string: ")

# Initialize a counter
vowel_count = 0

# Define vowels
vowels = "aeiouAEIOU"

# Loop through each character in the string
for char in text:
    if char in vowels:   # Check if the character is a vowel
        vowel_count += 1

# Print the result
print("Number of vowels:", vowel_count)