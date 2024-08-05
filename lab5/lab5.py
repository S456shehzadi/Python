from collections import deque

def bfs(graph, start_node, goal_node):
    visited = set()
    queue = deque([start_node])

    while queue:
        current_node = queue.popleft()
        print(f"Visiting: {current_node}")

        if current_node == goal_node:
            print(f"Goal node {goal_node} found!")
            return

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    print("Goal node not found.")

# Example graph
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

bfs(graph, start_node, goal_node)


#TASK NUMBER 2

import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

# Example usage of PriorityQueue
pq = PriorityQueue()
pq.put("A", 2)
pq.put("B", 1)
pq.put("C", 3)

while not pq.is_empty():
    print(pq.get())
