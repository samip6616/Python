# 1. Creating Dictionaries
print("1. Creating Dictionaries:")
dict_a = {'name': 'Alice', 'age': 30, 'city': 'New York'}
dict_b = dict([(1, 'one'), (2, 'two'), (3, 'three')])
print("Dictionary A:", dict_a)
print("Dictionary B:", dict_b)

# 2. Accessing Values
print("\n2. Accessing Values:")
print("Name from Dictionary A:", dict_a['name'])
print("Age from Dictionary A:", dict_a.get('age'))
# Using get with a default value
print("Country from Dictionary A (default):", dict_a.get('country', 'Not Found'))

# 3. Modifying Dictionaries
print("\n3. Modifying Dictionaries:")
dict_a['age'] = 31  # Update age
dict_a['country'] = 'USA'  # Add new key-value pair
print("Updated Dictionary A:", dict_a)

# 4. Deleting Entries
print("\n4. Deleting Entries:")
del dict_a['city']  # Remove city
print("Dictionary A after deletion:", dict_a)

# 5. Dictionary Comprehensions
print("\n5. Dictionary Comprehensions:")
squares = {x: x**2 for x in range(1, 6)}  # Create a dictionary of squares
print("Squares Dictionary:", squares)

# 6. Merging Dictionaries
print("\n6. Merging Dictionaries:")
dict_c = {'color': 'red', 'shape': 'circle'}
merged_dict = {**dict_a, **dict_c}  # Merge with unpacking
print("Merged Dictionary:", merged_dict)

# 7. Using Default Dictionary
from collections import defaultdict

print("\n7. Using Default Dictionary:")
default_dict = defaultdict(int)
for key in ['a', 'b', 'c', 'a', 'b', 'a']:
    default_dict[key] += 1
print("Default Dictionary:", default_dict)

# 8. Using Dictionary for Counting
print("\n8. Dictionary for Counting:")
word_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
word_count = {}
for word in word_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print("Word Count Dictionary:", word_count)

# 9. Nested Dictionaries
print("\n9. Nested Dictionaries:")
nested_dict = {
    'employee': {
        'name': 'John',
        'age': 28,
        'department': 'Sales'
    },
    'customer': {
        'name': 'Jane',
        'age': 34,
        'purchase_history': ['item1', 'item2']
    }
}
print("Nested Dictionary:", nested_dict)
print("Employee Name:", nested_dict['employee']['name'])

# 10. Dictionary for Storing Functions
print("\n10. Dictionary for Storing Functions:")
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

operation = {
    'add': add,
    'subtract': subtract
}

result_add = operation['add'](5, 3)
result_subtract = operation['subtract'](5, 3)
print("Addition Result:", result_add)
print("Subtraction Result:", result_subtract)

# 11. Using Named Tuples in a Dictionary
from collections import namedtuple

print("\n11. Using Named Tuples in a Dictionary:")
Student = namedtuple('Student', ['name', 'age', 'grade'])
students_dict = {
    'Alice': Student('Alice', 20, 'A'),
    'Bob': Student('Bob', 21, 'B'),
}

for name, student in students_dict.items():
    print(f"Student Name: {student.name}, Age: {student.age}, Grade: {student.grade}")

# 12. Dictionary Iteration
print("\n12. Dictionary Iteration:")
for key, value in merged_dict.items():
    print(f"{key}: {value}")

# 13. Sorting a Dictionary by Values
print("\n13. Sorting a Dictionary by Values:")
sorted_word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))
print("Sorted Word Count Dictionary:", sorted_word_count)

# 14. JSON Serialization
import json

print("\n14. JSON Serialization:")
json_dict = json.dumps(word_count)
print("JSON String of Word Count Dictionary:", json_dict)