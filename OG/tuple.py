# 1. Creating Tuples
print("1. Creating Tuples:")
empty_tuple = ()  # Empty tuple
single_element_tuple = (42,)  # Single element tuple
normal_tuple = (1, 2, 3, 4, 5)  # Normal tuple
mixed_tuple = (1, "Hello", 3.14, True, [1, 2])  # Mixed data types

print("Empty Tuple:", empty_tuple)
print("Single Element Tuple:", single_element_tuple)
print("Normal Tuple:", normal_tuple)
print("Mixed Tuple:", mixed_tuple)

# 2. Accessing Elements
print("\n2. Accessing Elements:")
print("First element of normal_tuple:", normal_tuple[0])
print("Last element of normal_tuple:", normal_tuple[-1])  # Negative index

# 3. Slicing Tuples
print("\n3. Slicing Tuples:")
print("Slice of normal_tuple [1:4]:", normal_tuple[1:4])

# 4. Immutability
print("\n4. Immutability:")
try:
    normal_tuple[0] = 100  # Attempting to change the tuple
except TypeError as e:
    print("Error:", e)

# 5. Packing and Unpacking
print("\n5. Packing and Unpacking:")
packed = (1, 2, 3)
a, b, c = packed  # Unpacking
print("Unpacked values:", a, b, c)

# 6. Using Tuples in Functions
print("\n6. Using Tuples in Functions:")
def return_tuple():
    return (10, 20, 30)

result = return_tuple()
print("Returned tuple from function:", result)

# 7. Tuples as Keys in Dictionaries
print("\n7. Tuples as Keys in Dictionaries:")
location = {}
location[(10.0, 20.0)] = "Point A"
location[(30.0, 40.0)] = "Point B"
print("Location Dictionary with Tuple Keys:", location)

# 8. Tuple Methods
print("\n8. Tuple Methods:")
example_tuple = (1, 2, 3, 2, 3, 2)
print("Count of 2 in example_tuple:", example_tuple.count(2))
print("Index of first occurrence of 3:", example_tuple.index(3))

# 9. Nested Tuples
print("\n9. Nested Tuples:")
nested_tuple = ((1, 2), (3, 4), (5, 6))
print("Nested Tuple:", nested_tuple)
print("Accessing nested element:", nested_tuple[1][0])  # Output: 3

# 10. Tuples and List Conversion
print("\n10. Converting Tuple to List and Back:")
tuple_to_list = list(normal_tuple)  # Convert to list
print("Tuple converted to List:", tuple_to_list)
list_to_tuple = tuple(tuple_to_list)  # Convert back to tuple
print("List converted back to Tuple:", list_to_tuple)

# 11. Tuple Operations
print("\n11. Tuple Operations:")
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2  # Concatenation
print("Combined Tuple:", combined_tuple)
repeated_tuple = tuple1 * 3  # Repetition
print("Repeated Tuple:", repeated_tuple)

# 12. Tuple in Loops
print("\n12. Tuple in Loops:")
for index, value in enumerate(normal_tuple):
    print(f"Index: {index}, Value: {value}")

# 13. Using Tuple as Return Types
print("\n13. Using Tuple as Return Types:")
def min_max(values):
    return (min(values), max(values))

numbers = [5, 2, 9, 1, 7]
minimum, maximum = min_max(numbers)
print("Minimum:", minimum, "Maximum:", maximum)

# 14. Named Tuples
from collections import namedtuple

print("\n14. Named Tuples:")
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print("Named Tuple:", p)
print("X coordinate:", p.x, "Y coordinate:", p.y)