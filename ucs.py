print("Hi Im learning git")
graph = {'S': [('A', 1), ('B', 4), ('D', 5)],
         'A': [('C', 8)],
         'B': [('D', 2)],
         'C': [('D', 1), ('G', 2)],
         'D': [('G', 7)],
         'G': []}


def cost_of_path(path):
    total = 0
    for (node, cost) in path:
        total += cost
    return total, path[-1][0]


def ucs(graph, start, goal):
    visited = []
    queue = [[(start, 0)]]
    while queue:
        queue.sort(key=cost_of_path)
        path = queue.pop(0)
        node = path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path
        else:
            adj = graph.get(node, [])
            for(node2, cost) in adj:
                current_path = path.copy()
                current_path.append((node2, cost))
                queue.append(current_path)


ans = ucs(graph, 'A', 'G')
print("Path: ", ans)
print("Cost of the above path: ", cost_of_path(ans)[0])
