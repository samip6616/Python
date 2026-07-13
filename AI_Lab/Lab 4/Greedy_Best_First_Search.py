# Lab: Greedy Best-First Search
# Program by: Samip Khadka
# Roll no: 36
# Step 1: Define the Graph (connections between nodes)
graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['F', 'G'],
    'E': ['G'],
    'F': [],
    'G': []
}
# Step 2: Define Heuristic Values (estimated distance to goal G)
heuristic = {
    'S': 10,
    'A': 8,
    'B': 6,
    'C': 5,
    'D': 4,
    'E': 3,
    'F': 2,
    'G': 0
}
# Step 3: Greedy BFS Algorithm
def greedy_bfs(start, goal):
    # Queue stores (h_value, node, path)
    queue = [(heuristic[start], start, [start])]
    visited = []

    print("=" * 62)
    print("GREEDY BEST-FIRST SEARCH")
    print("=" * 62)
    print(f"{'Step':<6}{'Current Node':<15}{'h(n)':<8}{'Path'}")
    print("-" * 62)

    step = 1

    while queue:
        # Sort by heuristic value
        queue.sort()

        # Remove node with smallest heuristic
        h_val, current, path = queue.pop(0)

        if current in visited:
            continue

        # Print current step
        print(f"{step:<6}{current:<15}{h_val:<8}{' -> '.join(path)}")
        step += 1

        # Goal reached
        if current == goal:
            print("=" * 62)
            print("GOAL FOUND!")
            print("Path :", " -> ".join(path))
            return path

        visited.append(current)

        # Add neighbours
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append((heuristic[neighbor], neighbor, path + [neighbor]))

    print("Goal not found!")
    return None
greedy_bfs('S', 'G')
print("Program by: Samip Khadka")
print("Roll No: 36")
