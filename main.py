from collections import deque

def bfs_shortest_path(graph, start, goal):
    # Validate inputs
    if start not in graph or goal not in graph:
        return []
    if start == goal:
        return [start]

    visited = {start}
    parent = {start: None}
    queue = deque([start])

    # BFS
    while queue:
        node = queue.popleft()
        if node == goal:
            break
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                queue.append(neighbor)

    # If goal unreachable
    if goal not in parent:
        return []

    # Reconstruct path
    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return path