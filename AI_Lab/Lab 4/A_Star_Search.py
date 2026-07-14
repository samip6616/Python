# Lab: A* Search Algorithm
# Program by: Samip Khadka
# Roll no: 36
import heapq

# Graph: (Neighbor, Cost)
graph = {
    'S': [('A', 5), ('B', 4)],
    'A': [('C', 3), ('D', 2)],
    'B': [('D', 2), ('E', 3)],
    'C': [('F', 2)],
    'D': [('F', 1), ('G', 2)],
    'E': [('G', 2)],
    'F': [],
    'G': []
}

# Heuristic values
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

def a_star(start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], 0, start, [start]))
    visited = {}

    print("=" * 73)
    print("A* SEARCH ALGORITHM")
    print("=" * 73)
    print(f"Start Node: {start}")
    print(f"Goal Node : {goal}\n")

    print("{:<5} {:<13} {:<6} {:<6} {:<6} {}".format(
        "Step", "Current Node", "g(n)", "h(n)", "f(n)", "Path"))
    print("-" * 73)

    step = 1

    while open_list:
        f, g, current, path = heapq.heappop(open_list)

        if current in visited and visited[current] <= g:
            continue

        visited[current] = g

        print("{:<5} {:<13} {:<6} {:<6} {:<6} {}".format(
            step,
            current,
            g,
            heuristic[current],
            f,
            " -> ".join(path)
        ))
        step += 1

        if current == goal:
            print("\n" + "=" * 73)
            print("GOAL FOUND!")
            print("=" * 73)
            print("Optimal Path :", " -> ".join(path))
            print("Total Cost   :", g)
            return

        for neighbor, cost in graph[current]:
            new_g = g + cost
            new_f = new_g + heuristic[neighbor]
            heapq.heappush(open_list,
                           (new_f, new_g, neighbor, path + [neighbor]))
a_star('S', 'G')
print("Program by: Samip Khadka")
print("Roll No: 36")
