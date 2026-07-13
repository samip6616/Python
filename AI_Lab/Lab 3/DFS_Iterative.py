# Lab: Depth-First Search (DFS) - Iterative
# Program by: Samip Khadka
# Roll no: 36

graph = {
'A': ['B', 'C'],
'B': ['D', 'E'],
'C': ['F'],
'D': ['G', 'H'],
'E': ['I'],
'F': ['J'],
'G': [],
'H': [],
'I': [],
'J': []
}

visited = []  # List for visited nodes
stack = []    # Initialize a stack

def dfs_iterative(visited, graph, node):
    stack.append(node)
    visited.append(node)

    while stack:
        m = stack.pop()
        print(m, end=' ')

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                stack.append(neighbour)
    return visited, stack

print("=" * 50)
print("DEPTH-FIRST SEARCH TRAVERSAL (ITERATIVE)")
print("=" * 50)
print("DFS Order: ", end='')

visited, stack = dfs_iterative(visited, graph, 'A')

print()  # Adds a new line right after the BFS traversal characters print out
print()  # Adds an extra blank line for visual spacing
print("Visited Nodes: ", visited)
print("Stack: ", stack)
print()
print("=" * 50)
print("Program by: Samip Khadka")
print("Roll No: 36")
