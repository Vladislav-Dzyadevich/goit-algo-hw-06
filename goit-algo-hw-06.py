import networkx as nx
import matplotlib.pyplot as plt

# Створення пустого графа
G = nx.Graph()

# Додавання вузлів (людей)
G.add_nodes_from(["Анна", "Борис", "Василь", "Галина", "Дмитро", "Євгенія", "Жанна"])

# Додавання ребер (дружба)
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

# Візуалізація графа
nx.draw(G, with_labels=True, node_color='lightblue', node_size=1500, font_size=10, font_weight='bold')
plt.title("Соціальна мережа друзів")
plt.show()

# Аналіз основних характеристик графа
print("Кількість вузлів (людей):", G.number_of_nodes())
print("Кількість ребер (дружба):", G.number_of_edges())
print("Ступінь кожного вузла (людини):")
print(dict(G.degree()))
