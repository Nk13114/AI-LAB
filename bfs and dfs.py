from collections import deque


def bfs(graph, start, goal):
    queue = deque([[start]])  # Store paths instead of just nodes
    visited = set()


    while queue:
        path = queue.popleft()
        node = path[-1]


        if node in visited:
            continue
        visited.add(node)


        # If goal is reached, return the path
        if node == goal:
            return path


        # Explore neighbors
        for neighbor in graph.get(node, []):
            new_path = list(path)
            new_path.append(neighbor)
            queue.append(new_path)
    
    return "No path found"


# Example Graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}


# Run BFS
start_node = 'A'
goal_node = 'H'
print("BFS Path:", bfs(graph, start_node, goal_node))




DFS
def dfs(graph, start, goal, path=None, visited=None):
    if path is None:
        path = [start]
    if visited is None:
        visited = set()


    visited.add(start)


    if start == goal:
        return path  # Return the found path


    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            new_path = dfs(graph, neighbor, goal, path + [neighbor], visited)
            if new_path:
                return new_path  # Return the first found path


    return None  # No path found


# Run DFS
print("DFS Path:", dfs(graph, start_node, goal_node))