import time
from collections import deque
import matplotlib.pyplot as plt
import networkx as nx


def bfs(graph, start_node) -> list[int]:
    visited = set()
    order: list[int] = []
    queue = deque([start_node])

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")
        if vertex not in visited:
            visited.add(vertex)
            order.append(vertex)
            for vertex_neighbor in graph[vertex]:
                if vertex_neighbor not in visited:
                    queue.append(vertex_neighbor)

    return order


def visualize_search(order, G, pos):
    for i, node in enumerate(order, start=1):
        plt.clf()
        plt.title(f"BFS Search - Step {i}")
        nx.draw(G, pos, with_labels=True, node_color=["red" if n == node else "blue" for n in G.nodes()])
        plt.draw()
        plt.pause(1)
    plt.show()
    time.sleep(1.5)


def main():
    G = nx.Graph()
    G.add_edges_from([
        (0, 1), (0, 2), (0, 3), (1, 4), (1, 5), (2, 6), (2, 7), (3, 8), (3, 9),
        (1, 10), (10, 11), (11, 12), (11, 13)
    ])
    pos = nx.spring_layout(G)
    order = bfs(G, 0)
    visualize_search(order, G, pos)


if __name__ == "__main__":
    main()