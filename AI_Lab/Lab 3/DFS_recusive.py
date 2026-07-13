# Lab: Depth-First Search (DFS) - Recursive
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

def dfs_recursive(visited, graph, node):
    if node not in visited:
        visited.append(node)
        print(node, end=' ')
        
        for neighbour in graph[node]:
            dfs_recursive(visited, graph, neighbour)

print("=" * 50)
print("DEPTH-FIRST SEARCH TRAVERSAL (RECURSIVE)")
print("=" * 50)
print("DFS Order: ", end='')
dfs_recursive(visited, graph, 'A')
print()
print("=" * 50)
print("Program by: Samip Khadka")
print("Roll No: 36")
