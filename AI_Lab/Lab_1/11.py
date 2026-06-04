# Take age as input from the user
age = int(input("Enter your age: "))

# Check if the person is eligible to vote
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Check if the person is a senior citizen
if age >= 60:
    print("You are a senior citizen.")
else:
    print("You are not a senior citizen.")