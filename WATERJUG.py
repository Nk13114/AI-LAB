from collections import deque


def is_valid_state(state, X, Y, visited):
    return 0 <= state[0] <= X and 0 <= state[1] <= Y and state not in visited


def water_jug_bfs(X, Y, Z):
    if Z > max(X, Y):
        return "Impossible to measure"


    queue = deque([(0, 0)])  # (Jug1, Jug2)
    visited = set()
    parent = {}  # To track steps
    solution_found = False


    while queue:
        jug1, jug2 = queue.popleft()
        visited.add((jug1, jug2))


        # If we reach the target amount
        if jug1 == Z or jug2 == Z:
            solution_found = True
            break


        # Possible moves
        moves = [
            (X, jug2),  # Fill jug1
            (jug1, Y),  # Fill jug2
            (0, jug2),  # Empty jug1
            (jug1, 0),  # Empty jug2
            (jug1 - min(jug1, Y - jug2), jug2 + min(jug1, Y - jug2)),  # Pour jug1 -> jug2
            (jug1 + min(jug2, X - jug1), jug2 - min(jug2, X - jug1)),  # Pour jug2 -> jug1
        ]


        for new_state in moves:
            if is_valid_state(new_state, X, Y, visited):
                queue.append(new_state)
                visited.add(new_state)
                parent[new_state] = (jug1, jug2)


    # If solution found, trace back steps
    if solution_found:
        path = []
        current = (jug1, jug2)
        while current in parent:
            path.append(current)
            current = parent[current]
        path.append((0, 0))
        path.reverse()
        return path
    else:
        return "No solution found"


# Example usage
X = 4  # Capacity of first jug
Y = 3  # Capacity of second jug
Z = 2  # Target amount


solution = water_jug_bfs(X, Y, Z)
print("Steps to reach", Z, "liters:")
for step in solution:
    print(step)