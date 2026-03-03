'''Build Undirected Graph & Shortest Path
Use dictionaries to build an undirected graph and find the shortest path between two nodes.
Input: edges = [('A', 'B'), ('B', 'C'), ('A', 'C')], start = 'A', end = 'C'
Expected Output: ['A', 'C']'''

from collections import deque, defaultdict

edges = [('A', 'B'), ('B', 'C'), ('A', 'C')]
start = 'A'
end = 'C'

graph = defaultdict(list)

for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)  

def shortest_path(graph, start, end):
    visited = set()
    queue = deque([[start]]) 

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == end:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                new_path = path + [neighbor]
                queue.append(new_path)

    return None  

result = shortest_path(graph, start, end)
print(result)
