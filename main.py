from collections import deque
import heapq


def bfs_shortest_path(graph, start, goal):
    # Keep track of explored nodes
    explored = set()
    # Keep track of all the paths to be checked
    queue = deque([[start]])

    # Return path if start is goal
    if start == goal:
        return [start]

    # Loop to traverse the graph with the help of the queue
    while queue:
        # Pop the first path from the queue
        path = queue.popleft()
        # Get the last node from the path
        node = path[-1]

        if node not in explored:
            neighbours = graph[node]
            # Go through all neighbour nodes, construct a new path and push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # Return path if neighbour is goal
                if neighbour == goal:
                    return new_path

            # Mark node as explored
            explored.add(node)

    # In case there's no path between the 2 nodes
    return "No path found"


# Define the graph
graph = {
    'A': ['B', 'D'],
    'B': ['C', 'E'],
    'C': ['F'],
    'D': ['E', 'G'],
    'E': ['F', 'H'],
    'F': ['I'],
    'G': ['H'],
    'H': ['I'],
    'I': []
}

# Example usage
start = 'A'
goal = 'I'
print(f"Shortest path from {start} to {goal}: {bfs_shortest_path(graph, start, goal)}")


print("##############################################")



def ucs(graph, start, goal):
    # priority queue to store (cost, path)
    queue = [(0, [start])]
    visited = set()

    while queue:

        cost, path = heapq.heappop(queue)
        node = path[-1]

        if node == goal:
            return path, cost

        if node not in visited:
            visited.add(node)

            for neighbour, edge_cost in graph.get(node, []):
                if neighbour not in visited:
                    new_cost = cost + edge_cost
                    new_path = path + [neighbour]
                    heapq.heappush(queue, (new_cost, new_path))

    return "No path found"

graph = {
    'A': [('B', 4), ('D', 3)],
    'B': [('C', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [('G', 2), ('E', 6)],
    'E': [('H', 3), ('F', 2)],
    'F': [('I', 1)],
    'G': [('H', 2)],
    'H': [('I', 4)],
    'I': []
}


start = 'A'
goal = 'F'
path, cost = ucs(graph, start, goal)
print(f"Least-cost path from {start} to {goal}: {path} with cost {cost}")

print("##############################################")


def is_valid(board, row, col):
    for r in range(row):
        c = board[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True

def solve_n_queens(n):
    solutions = []
    stack = [(0, [1, -1, -1, -1])]  # Start with the initial board configuration

    while stack:
        row, board = stack.pop()
        if row == n:
            solutions.append(board)
        else:
            for col in range(n):
                if is_valid(board, row, col):
                    new_board = board[:]
                    new_board[row] = col
                    stack.append((row + 1, new_board))

    return solutions

def print_board(board):
    n = len(board)
    for row in board:
        line = ['.'] * n
        if row != -1:
            line[row] = 'Q'
        print(' '.join(line))
    print()

# Solve the 4-Queens problem
solutions = solve_n_queens(4)
print(f"Total solutions: {len(solutions)}")
for solution in solutions:
    print_board(solution)