from collections import deque


# Define possible actions the monkey can take
ACTIONS = ["move left", "move right", "push box left", "push box right", "climb box", "grab bananas"]


# BFS function to find the shortest path to bananas
def monkey_banana_bfs(start_state):
    queue = deque([(start_state, [])])  # (state, path to reach state)
    visited = set()


    while queue:
        (monkey, box, has_banana), path = queue.popleft()


        # Goal state: monkey reaches banana
        if has_banana:
            return path + ["Monkey grabs the bananas! 🍌"]


        if (monkey, box, has_banana) in visited:
            continue
        visited.add((monkey, box, has_banana))


        # Possible moves
        new_states = []


        # Move left/right if not at the edges (0-4 grid)
        if monkey > 0:
            new_states.append(((monkey - 1, box, has_banana), path + ["Move left"]))
        if monkey < 4:
            new_states.append(((monkey + 1, box, has_banana), path + ["Move right"]))


        # Push the box
        if monkey == box:
            if box > 0:
                new_states.append(((monkey - 1, box - 1, has_banana), path + ["Push box left"]))
            if box < 4:
                new_states.append(((monkey + 1, box + 1, has_banana), path + ["Push box right"]))


        # Climb the box
        if monkey == box:
            new_states.append(((monkey, box, True), path + ["Climb the box"]))


        # Add new states to queue
        queue.extend(new_states)


    return "No solution found"


# Initial state: (Monkey position, Box position, Has banana?)
initial_state = (0, 2, False)  # Monkey at 0, Box at 2, Monkey doesn't have banana


# Run BFS to find solution
solution = monkey_banana_bfs(initial_state)


# Print the sequence of steps
print("Steps to get the bananas:")
for step in solution:
    print(step)