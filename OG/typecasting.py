# type casting = The process of converting a value of one data type to another
#                          (string, integer, float, boolean)
#                          Explicit vs Implicit

name = "Samip"
age = 19
gpa = 3.3
student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(student)) 

age = float(age)
print(age)

gpa = int(gpa)
print(gpa)

student = str(student)
print(student)

name = bool(name)
print(name)