import networkx as nx

def dijkstra(graph, start):
    # Ініціалізація відстаней до всіх вершин як нескінченні
    distances = {node: float('inf') for node in graph.nodes()}
    # Відстань до початкової вершини ставимо рівною 0
    distances[start] = 0

    # Ініціалізуємо множину відвіданих вершин
    visited = set()

    while len(visited) < len(graph.nodes()):
        # Знаходимо вершину з найменшою відстанню, яка ще не була відвідана
        min_distance = float('inf')
        for node in graph.nodes():
            if node not in visited and distances[node] < min_distance:
                min_distance = distances[node]
                current_node = node

        # Додаємо поточну вершину до відвіданих
        visited.add(current_node)

        # Оновлюємо відстані до всіх сусідніх вершин поточної вершини
        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            if distances[current_node] + weight < distances[neighbor]:
                distances[neighbor] = distances[current_node] + weight

    return distances

# Граф з вагами на ребрах
G = nx.Graph()
G.add_nodes_from(["Анна", "Борис", "Василь", "Галина", "Дмитро", "Євгенія", "Жанна"])
G.add_weighted_edges_from([
    ("Анна", "Борис", 2),
    ("Анна", "Василь", 5),
    ("Борис", "Василь", 3),
    ("Борис", "Галина", 6),
    ("Василь", "Галина", 1),
    ("Василь", "Дмитро", 4),
    ("Дмитро", "Євгенія", 7),
    ("Дмитро", "Жанна", 2)
])

# Виклик функції Дейкстри для знаходження найкоротших шляхів від кожної вершини до всіх інших
for node in G.nodes():
    shortest_paths = dijkstra(G, node)
    print(f"Найкоротші шляхи від вершини {node}:")
    print(shortest_paths)
    print()
