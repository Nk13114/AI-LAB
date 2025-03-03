from queue import PriorityQueue
import numpy as np


# Define the goal state
GOAL_STATE = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])


# Helper function to calculate the Manhattan Distance heuristic
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                x, y = divmod(state[i][j] - 1, 3)
                distance += abs(x - i) + abs(y - j)
    return distance


# Generate possible moves
def get_neighbors(state):
    neighbors = []
    x, y = np.where(state == 0)
    x, y = int(x), int(y)
    moves = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    
    for new_x, new_y in moves:
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = state.copy()
            new_state[x, y], new_state[new_x, new_y] = new_state[new_x, new_y], new_state[x, y]
            neighbors.append(new_state)
    
    return neighbors


# A* Search Algorithm
def solve_puzzle(initial_state):
    pq = PriorityQueue()
    pq.put((manhattan_distance(initial_state), 0, initial_state, []))
    visited = set()
    
    while not pq.empty():
        _, cost, state, path = pq.get()
        
        if np.array_equal(state, GOAL_STATE):
            return path
        
        visited.add(tuple(state.flatten()))
        
        for neighbor in get_neighbors(state):
            if tuple(neighbor.flatten()) not in visited:
                new_path = path + [neighbor]
                pq.put((cost + manhattan_distance(neighbor), cost + 1, neighbor, new_path))
    
    return None


# Example usage
initial_state = np.array([[1, 2, 3], [0, 4, 6], [7, 5, 8]])
solution = solve_puzzle(initial_state)


if solution:
    print("Solution found in", len(solution), "steps:")
    for step in solution:
        print(step, "\n")
else:
    print("No solution found")