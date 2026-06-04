# Take marks from the user
marks = float(input("Enter your marks (0-100): "))

# Check conditions and assign grades
if marks >= 90 and marks <= 100:
    print("Grade: A")
elif marks >= 80 and marks <= 89:
    print("Grade: B")
elif marks >= 70 and marks <= 79:
    print("Grade: C")
elif marks >= 60 and marks <= 69:
    print("Grade: D")
elif marks < 60:
    print("Grade: F")
else:
    print("Invalid marks entered")