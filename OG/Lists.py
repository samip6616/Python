# Define a list of mixed data types
mixed_list = [1, 2.5, 'Hello', True, [5, 6], None]

# 1. Creating Lists
print("1. Creating Lists:")
numbers = [i for i in range(1, 11)]  # List of numbers from 1 to 10
print("Numbers:", numbers)

# 2. Accessing Elements
print("\n2. Accessing Elements:")
print("First element:", numbers[0])
print("Last element:", numbers[-1])  # Negative index for last element

# 3. Slicing Lists
print("\n3. Slicing Lists:")
print("First three elements:", numbers[:3])
print("Last three elements:", numbers[-3:])

# 4. Modifying Lists
print("\n4. Modifying Lists:")
numbers[0] = 100  # Update first element
print("Updated numbers:", numbers)

# 5. Adding Elements
print("\n5. Adding Elements:")
numbers.append(11)  # Add element at the end
print("After appending 11:", numbers)
numbers.insert(0, 0)  # Insert element at index 0
print("After inserting 0 at index 0:", numbers)

# 6. Removing Elements
print("\n6. Removing Elements:")
removed_element = numbers.pop()  # Remove the last element
print(f"Removed element: {removed_element}")
print("After popping last element:", numbers)
numbers.remove(100)  # Remove specific element
print("After removing 100:", numbers)

# 7. List Comprehensions
print("\n7. List Comprehensions:")
squares = [x**2 for x in numbers]  # List of squares
print("Squares of numbers:", squares)

# 8. Sorting Lists
print("\n8. Sorting Lists:")
numbers.sort()  # Sort the list
print("Sorted numbers:", numbers)

# 9. Reversing a List
print("\n9. Reversing a List:")
numbers.reverse()  # Reverse the list
print("Reversed numbers:", numbers)

# 10. Nested Lists
print("\n10. Nested Lists:")
nested_list = [[1, 2], [3, 4], [5, 6]]  # List of lists
print("Nested List:", nested_list)
print("Accessing nested element:", nested_list[1][0])  # Access element '3'

# 11. Using List Methods
print("\n11. Using List Methods:")
print("Count of 2 in numbers:", numbers.count(2))  # Count occurrences
print("Length of numbers:", len(numbers))  # Length of list

# 12. Concatenating Lists
print("\n12. Concatenating Lists:")
combined_list = numbers + squares  # Concatenate two lists
print("Combined List:", combined_list)

# 13. Copying a List
print("\n13. Copying a List:")
copied_list = numbers.copy()  # Create a copy of the list
print("Copied List:", copied_list)

# 14. List Membership
print("\n14. List Membership:")
print("Is 5 in numbers?", 5 in numbers)

# 15. Iterating through a List
print("\n15. Iterating through a List:")
print("Numbers:")
for num in numbers:
    print(num, end=' ')
print()  # Newline after printing numbers

# 16. Flattening a Nested List
print("\n16. Flattening a Nested List:")
flat_list = [item for sublist in nested_list for item in sublist]
print("Flattened List:", flat_list)

# 17. Finding Minimum and Maximum
print("\n17. Finding Minimum and Maximum:")
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))

# 18. Using List as a Queue
from collections import deque
queue = deque(numbers)  # Create a deque from numbers for queue operations
queue.append(12)  # Add to the end of the queue
print("\nUsing List as a Queue:")
print("Queue after adding 12:", list(queue))
print("Removed from queue:", queue.popleft())  # Remove from the front
print("Queue after removing an item:", list(queue))

# 19. List as a Stack
stack = []  # Create an empty stack (list)
stack.append(1)  # Push onto stack
stack.append(2)
print("\nUsing List as a Stack:")
print("Stack:", stack)
print("Popped from stack:", stack.pop())  # Pop from stack
print("Stack after popping:", stack)

# 20. List of Objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

persons = [Person("Alice", 28), Person("Bob", 34)]
print("\n20. List of Objects:")
for person in persons:
    print(f"Name: {person.name}, Age: {person.age}")