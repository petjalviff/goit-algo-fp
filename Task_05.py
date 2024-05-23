import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree, traversal_order, traversal_type):
    tree_graph = nx.DiGraph()
    pos = {tree.id: (0, 0)}
    tree_graph = add_edges(tree_graph, tree, pos)
    
    id_to_color = {node.id: color for node, color in zip(traversal_order, generate_color_gradient(len(traversal_order)))}
    for node in tree_graph.nodes:
        tree_graph.nodes[node]['color'] = id_to_color.get(node, "lightgray")
    
    colors = [node[1]['color'] for node in tree_graph.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree_graph.nodes(data=True)}

    plt.figure(figsize=(8, 6))
    if traversal_type == "DFS":
        traversal_type = "Обхід у глибину (DFS)"
    elif traversal_type == "BFS":
        traversal_type = "Обхід у ширину (BFS)"
    plt.title(f"{traversal_type}", pad=20)
    nx.draw(tree_graph, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.subplots_adjust(top=0.9, bottom=0.1)
    plt.show()


def generate_color_gradient(n):
    color_range = range(0, 256, int(256 / n))
    return [f"#{r:02x}{r:02x}ff" for r in color_range]

def dfs(node, visited=None):
    if visited is None:
        visited = []
    if node:
        visited.append(node)
        dfs(node.left, visited)
        dfs(node.right, visited)
    return visited

def bfs(root):
    visited, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        if node:
            visited.append(node)
            queue.append(node.left)
            queue.append(node.right)
    return visited

def build_min_heap(arr):
    n = len(arr)
    nodes = [Node(val) for val in arr]
    for i in range(n):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < n:
            nodes[i].left = nodes[left_index]
        if right_index < n:
            nodes[i].right = nodes[right_index]
    return nodes[0]

heap_array = [2, 3, 4, 5, 6, 7]
root = build_min_heap(heap_array)

dfs_nodes = dfs(root)
draw_tree(root, dfs_nodes, "DFS")

bfs_nodes = bfs(root)
draw_tree(root, bfs_nodes, "BFS")