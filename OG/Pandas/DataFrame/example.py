import pandas as pd

student = {
    "Name": ["Ram", "Hari", "Sita", "Gita"],
    "Age": [20, 21, 19, 22],
    "Marks": [85, 90, 95, 88]
}

df = pd.DataFrame(student)

print("Student Data")
print(df)

print("\nAverage Marks:", df["Marks"].mean())

print("\nStudents scoring above 88:")
print(df[df["Marks"] > 88])

df["Grade"] = ["B", "A", "A", "B"]

print("\nUpdated DataFrame")
print(df)
