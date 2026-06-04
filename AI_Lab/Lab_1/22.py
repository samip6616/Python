# Function to convert marks into grades
def get_grade(marks):
    if marks >= 90 and marks <= 100:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    elif marks >= 0:
        return "F"
    else:
        return "Invalid marks"

# Take input from the user
marks = float(input("Enter your marks (0-100): "))

# Call the function and print the result
grade = get_grade(marks)
print("Your grade is:", grade)