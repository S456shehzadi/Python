print("Task 1 greedy best first Solution")

import heapq

def greedy_best_first_search(graph, start, goal, heuristic):
    open_list = []
    closed_list = set()
    heapq.heappush(open_list, (heuristic[start], start))

    while open_list:
        _, current_node = heapq.heappop(open_list)

        if current_node in closed_list:
            continue

        print(f"Visiting: {current_node}")
        if current_node == goal:
            print("Goal reached!")
            return

        closed_list.add(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in closed_list:
                heapq.heappush(open_list, (heuristic[neighbor], neighbor))

    print("Goal not found.")

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': [],
    'H': []
}
heuristic = {
    'A': 7, 'B': 6, 'C': 3, 'D': 6, 'E': 2, 'F': 1, 'G': 0, 'H': 1
}
greedy_best_first_search(graph, 'A', 'G', heuristic)


print("Task 2  A* search Solution")

import heapq

def a_star_search(graph, start, goal, heuristic, costs):
    open_list = []
    closed_list = set()
    heapq.heappush(open_list, (heuristic[start], start))
    g_costs = {start: 0}

    while open_list:
        _, current_node = heapq.heappop(open_list)

        if current_node in closed_list:
            continue

        print(f"Visiting: {current_node}")
        if current_node == goal:
            print("Goal reached!")
            return

        closed_list.add(current_node)

        for neighbor, cost in graph[current_node]:
            tentative_g_cost = g_costs[current_node] + cost

            if neighbor not in closed_list and (neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]):
                g_costs[neighbor] = tentative_g_cost
                f_cost = tentative_g_cost + heuristic[neighbor]
                heapq.heappush(open_list, (f_cost, neighbor))

    print("Goal not found.")

# Example usage:
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 5)],
    'C': [('F', 1), ('G', 12)],
    'D': [],
    'E': [('H', 2)],
    'F': [],
    'G': [],
    'H': []
}
heuristic = {
    'A': 7, 'B': 6, 'C': 3, 'D': 6, 'E': 2, 'F': 1, 'G': 0, 'H': 1
}
a_star_search(graph, 'A', 'G', heuristic, costs=None)

print("Task 3  8 Puzzle Problem using A* Solution")

import heapq

class PuzzleState:
    def __init__(self, board, goal, empty_pos, g_cost=0):
        self.board = board
        self.goal = goal
        self.empty_pos = empty_pos
        self.g_cost = g_cost
        self.f_cost = self.g_cost + self.heuristic()

    def heuristic(self):
        # Heuristic: Number of misplaced tiles
        return sum(
            1 if self.board[i] != self.goal[i] and self.board[i] != 0 else 0
            for i in range(9)
        )

    def is_goal(self):
        return self.board == self.goal

    def get_neighbors(self):
        neighbors = []
        x, y = self.empty_pos
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_board = self.board[:]
                new_board[x * 3 + y], new_board[nx * 3 + ny] = new_board[nx * 3 + ny], new_board[x * 3 + y]
                neighbors.append(PuzzleState(new_board, self.goal, (nx, ny), self.g_cost + 1))

        return neighbors

    def __lt__(self, other):
        return self.f_cost < other.f_cost

def a_star_puzzle_solver(start, goal):
    open_list = []
    closed_list = set()
    initial_state = PuzzleState(start, goal, start.index(0))
    heapq.heappush(open_list, initial_state)

    while open_list:
        current_state = heapq.heappop(open_list)

        if current_state.is_goal():
            print("Goal reached!")
            print(current_state.board)
            return

        closed_list.add(tuple(current_state.board))

        for neighbor in current_state.get_neighbors():
            if tuple(neighbor.board) not in closed_list:
                heapq.heappush(open_list, neighbor)

    print("No solution found.")

# Example usage:
start_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
a_star_puzzle_solver(start_state, goal_state)
