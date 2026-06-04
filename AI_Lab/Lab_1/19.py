
# Function to check if a number is even or odd
def check_even_odd(num):
    if num % 2 == 0:     # If remainder when divided by 2 is 0
        return "Even"
    else:
        return "Odd"

# Take input from the user
number = int(input("Enter a number: "))

# Call the function and print the result
result = check_even_odd(number)
print("The number is:", result)