import time
from collections import deque
import matplotlib.pyplot as plt
import networkx as nx


def dfs_stack(graph, start_node) -> list[int]:
    visited = set()
    order: list[int] = []
    queue = deque([start_node])

    while queue:
        vertex = queue.pop()
        print(vertex, end=" ")
        if vertex not in visited:
            visited.add(vertex)
            order.append(vertex)
            print(graph[vertex])
            for vertex_neighbor in graph[vertex]:
                if vertex_neighbor not in visited:
                    queue.append(vertex_neighbor)

    return order


def dfs_recursive(graph, start_node, visited=None) -> list[int]:
    if visited is None:
        visited = set()

    order = []

    if start_node not in visited:
        visited.add(start_node)
        order.append(start_node)
        print(start_node, end=" ")
        print(graph[start_node])
        for vertex_neighbor in graph[start_node]:
            if vertex_neighbor not in visited:
                order.extend(dfs_recursive(graph, vertex_neighbor, visited))

    return order


def visualize_search(order, G, pos, title="DFS Search"):
    for i, node in enumerate(order, start=1):
        plt.clf()
        plt.title(f"{title} - Step {i}")
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
    order_stack = dfs_stack(G, 0)
    visualize_search(order_stack, G, pos, title="DFS Stack")

    order_recursive = dfs_recursive(G, 0)
    visualize_search(order_recursive, G, pos, title="DFS Recursive")


if __name__ == "__main__":
    main()