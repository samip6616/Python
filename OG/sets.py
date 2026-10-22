# 1. Creating Sets
print("1. Creating Sets:")
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print("Set A:", set_a)
print("Set B:", set_b)

# 2. Basic Set Operations: Union, Intersection, Difference
print("\n2. Basic Set Operations:")
union_set = set_a.union(set_b)
intersection_set = set_a.intersection(set_b)
difference_set = set_a.difference(set_b)

print("Union of Set A and B:", union_set)
print("Intersection of Set A and B:", intersection_set)
print("Difference (A - B) of Set A and B:", difference_set)

# 3. Adding and Removing Elements
print("\n3. Adding and Removing Elements:")
set_a.add(6)  # Adding an element
print("Set A after adding 6:", set_a)

set_a.remove(2)  # Removing an element
print("Set A after removing 2:", set_a)

# 4. Set Comprehensions
print("\n4. Set Comprehensions:")
squares = {x**2 for x in range(10)}  # Set of squares
print("Set of squares from 0-9:", squares)

# 5. Checking Subset and Superset
print("\n5. Checking Subset and Superset:")
print("Is Set B a subset of Set A?", set_b.issubset(set_a))
print("Is Set A a superset of Set B?", set_a.issuperset(set_b))

# 6. Using Sets for Unique Data
print("\n6. Using Sets for Unique Data:")
data_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
unique_data = set(data_with_duplicates)  # Remove duplicates
print("Unique data from list:", unique_data)

# 7. Set Intersection with Condition
print("\n7. Set Intersection with Condition:")
evens = {x for x in range(10) if x % 2 == 0}
print("Even numbers set:", evens)
print("Intersection with Set A:", evens.intersection(set_a))

# 8. Frozenset for Immutability
print("\n8. Using Frozenset for Immutability:")
frozen_set = frozenset([1, 2, 3])
print("Frozenset:", frozen_set)
# frozen_set.add(4)  # This will raise an AttributeError

# 9. Set Operations in Functions
print("\n9. Set Operations in Functions:")
def set_operations(x, y):
    return x.union(y), x.intersection(y)

union_result, intersection_result = set_operations(set_a, set_b)
print("Union from function:", union_result)
print("Intersection from function:", intersection_result)

# 10. Using Sets in Graph Problems
print("\n10. Using Sets in Graph Problems:")
# Example: Finding connected components in an undirected graph
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D'},
    'C': {'A'},
    'D': {'B', 'E'},
    'E': {'D'},
}

def find_connected_components(graph):
    visited = set()
    components = []

    def dfs(node, component):
        visited.add(node)
        component.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, component)

    for node in graph:
        if node not in visited:
            component = set()
            dfs(node, component)
            components.append(component)

    return components

connected_components = find_connected_components(graph)
print("Connected components in the graph:", connected_components)

# 11. Set as a Collection of Objects
print("\n11. Set as a Collection of Objects:")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __hash__(self):
        return hash((self.name, self.age))

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

people = {Person("Alice", 30), Person("Bob", 25)}
print("Set of People:")
for person in people:
    print(f"Name: {person.name}, Age: {person.age}")