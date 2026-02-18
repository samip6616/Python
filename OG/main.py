''' Variable = A variable is a container for storing data values (string, integer, float, boolean, etc.)
 A variable behaves as if it was the value
'''
#Strings
first_name = "Bro"
food = "pizza"
email = "Bro123@fake.com"

#print(first_name)

print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is {email}")

#Integers
age = 21
quantity = 3
num_of_students = 30

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

# Float
price = 10.99
gpa = 3.2
distance = 5.5

print(f"The price is ${price}")
print(f"Your GPA is {gpa}")
print(f"You ran {distance} miles")

#Boolean
is_student = True
for_sale = False
is_online = True

if is_student:
    print("You are a student")
else:
    print("You are NOT student")

if for_sale:
    print("That item is for sale")
else:
    print("That item is NOT available")
if is_online:
    print("You are online")
else:
    print("You are NOT online")