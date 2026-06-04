# Function to find the maximum value in a list
def find_max(numbers):
    maximum = numbers[0]  # Assume first element is the largest
    for num in numbers:
        if num > maximum:  # Compare each element
            maximum = num
    return maximum


# Function to find the minimum value in a list
def find_min(numbers):
    minimum = numbers[0]  # Assume first element is the smallest
    for num in numbers:
        if num < minimum:  # Compare each element
            minimum = num
    return minimum


# Example list (you can also take input from user)
numbers = [10, 5, 20, 8, 15]

# Call the functions
max_value = find_max(numbers)
min_value = find_min(numbers)

# Print results
print("Maximum value:", max_value)
print("Minimum value:", min_value)