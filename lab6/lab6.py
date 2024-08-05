
#TASK NUMBER 1

def dfs(graph, start_node, goal_node):
    stack = [start_node]
    visited = set()

    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            print(f"Visiting: {current_node}")
            visited.add(current_node)

            if current_node == goal_node:
                print(f"Goal node {goal_node} found!")
                return

            
            for neighbor in reversed(graph[current_node]):
                if neighbor not in visited:
                    stack.append(neighbor)

    print("Goal node not found.")


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

start_node = 'A'
goal_node = 'G'

dfs(graph, start_node, goal_node)



