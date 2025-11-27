from collections import deque

def bfs_shortest_path(graph, start, goal):
    """
    Find the shortest path in an unweighted graph using BFS.
    graph: dict {room: [neighbors]}
    start: starting room (string)
    goal: target room (string)
    Returns: list of rooms from start to goal, or [] if no path.
    """

    # Step 1: Handle invalid inputs
    if start not in graph or goal not in graph:
        return []

    # Step 2: Handle trivial case
    if start == goal:
        return [start]

    # Step 3: BFS setup
    visited = {start}
    parent = {start: None}
    queue = deque([start])

    # Step 4: BFS loop
    while queue:
        node = queue.popleft()
        if node == goal:
            break
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                queue.append(neighbor)

    # Step 5: Reconstruct path
    if goal not in parent:
        return []

    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()

    return path