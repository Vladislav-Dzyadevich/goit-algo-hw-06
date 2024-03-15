import networkx as nx

def dfs_paths(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next_node in graph.neighbors(start):
        if next_node not in path:
            yield from dfs_paths(graph, next_node, goal, path + [next_node])

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next_node in graph.neighbors(vertex):
            if next_node not in path:
                if next_node == goal:
                    yield path + [next_node]
                else:
                    queue.append((next_node, path + [next_node]))

# Граф, який був розроблений у першому завданні
G = nx.Graph()
G.add_nodes_from(["Анна", "Борис", "Василь", "Галина", "Дмитро", "Євгенія", "Жанна"])
G.add_edges_from([
    ("Анна", "Борис"),
    ("Анна", "Василь"),
    ("Борис", "Василь"),
    ("Борис", "Галина"),
    ("Василь", "Галина"),
    ("Василь", "Дмитро"),
    ("Дмитро", "Євгенія"),
    ("Дмитро", "Жанна")
])

# Пошук шляхів з використанням DFS
print("DFS Paths:")
for path in dfs_paths(G, "Анна", "Жанна"):
    print(path)

# Пошук шляхів з використанням BFS
print("\nBFS Paths:")
for path in bfs_paths(G, "Анна", "Жанна"):
    print(path)
