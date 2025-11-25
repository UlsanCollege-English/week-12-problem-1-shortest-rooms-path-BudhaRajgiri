from collections import deque

def bfs_shortest_path(graph, start, goal):
    if start not in graph or goal not in graph:
        return []
    if start == goal:
        return [start]

    queue = deque([[start]])
    visited = set([start])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return []