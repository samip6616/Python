# Function to check if a year is a leap year
def is_leap_year(year):
    # Conditions for a leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Take input from the user
year = int(input("Enter a year: "))

# Call the function and display result
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")