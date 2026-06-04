# Function to calculate the sum from 1 to n
def sum_upto_n(n):
    total = 0  # Initialize sum to 0

    # Loop from 1 to n
    for i in range(1, n + 1):
        total += i   # Add each number to total

    return total  # Return the final sum


# Take input from the user
num = int(input("Enter a number: "))

# Call the function and print the result
result = sum_upto_n(num)
print("The sum from 1 to", num, "is:", result)