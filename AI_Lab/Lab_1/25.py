# Function to count vowels and consonants
def count_vowels_consonants(text):
    vowels = "aeiouAEIOU"  # Define vowels
    vowel_count = 0
    consonant_count = 0

    # Loop through each character in the string
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count


# Take input from the user
string = input("Enter a string: ")

# Call the function
vowels, consonants = count_vowels_consonants(string)

# Print results
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)