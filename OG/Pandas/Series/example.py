import pandas as pd

marks = pd.Series(
    [85, 92, 78, 95],
    index=["Samidha", "Samira", "Sami", "Sonu"]
)

print("Marks:")
print(marks)

print("\nAverage =", marks.mean())
print("Maximum =", marks.max())

print("\nStudents scoring above 80:")
print(marks[marks > 80])
