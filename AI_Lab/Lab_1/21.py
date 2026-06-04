# Function to print multiplication table
def multiplication_table(num):
    # Loop from 1 to 10
    for i in range(1, 11):
        result = num * i
        print(num, "x", i, "=", result)


# Take input from the user
number = int(input("Enter a number: "))

# Call the function
multiplication_table(number)