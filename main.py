from collections import deque

def bfs_shortest_path(graph, start, goal):
    """
    Find the shortest path between start and goal in an unweighted graph using BFS.
    Returns [] if no path exists.
    """
    if start not in graph or goal not in graph:
        return []

    if start == goal:
        return [start]

    queue = deque([(start, [start])])
    visited = set()

    while queue:
        current, path = queue.popleft()

        if current in visited:
            continue
        visited.add(current)

        for neighbor in graph.get(current, []):
            new_path = path + [neighbor]
            if neighbor == goal:
                return new_path
            queue.append((neighbor, new_path))

    return []