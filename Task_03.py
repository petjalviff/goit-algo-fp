import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]
    
    def add_edge(self, src, dest, weight):
        self.graph[src].append((dest, weight))
        self.graph[dest].append((src, weight)) 

    def dijkstra(self, src):
        distances = [float('inf')] * self.V
        distances[src] = 0
        min_heap = [(0, src)]
        
        while min_heap:
            dist, u = heapq.heappop(min_heap)
            if dist > distances[u]:
                continue
            
            for neighbor, weight in self.graph[u]:
                if distances[u] + weight < distances[neighbor]:
                    distances[neighbor] = distances[u] + weight
                    heapq.heappush(min_heap, (distances[neighbor], neighbor))
        
        return distances

def print_distances(distances):
    print("Найкоротші шляхи від початкової вершини:")
    for i, d in enumerate(distances):
        print(f"Вершина {i}: Відстань {d}")

g = Graph(10)
g.add_edge(0, 1, 4)
g.add_edge(0, 7, 8)
g.add_edge(1, 2, 8)
g.add_edge(1, 7, 11)
g.add_edge(2, 3, 7)
g.add_edge(2, 8, 2)
g.add_edge(2, 5, 4)
g.add_edge(3, 4, 9)
g.add_edge(3, 5, 14)
g.add_edge(4, 5, 10)
g.add_edge(5, 6, 2)
g.add_edge(6, 7, 1)
g.add_edge(6, 8, 6)
g.add_edge(5, 8, 7)
g.add_edge(9, 6, 1)
g.add_edge(9, 1, 8)

distances = g.dijkstra(0)

print_distances(distances)

G = nx.Graph()

for u in range(len(g.graph)):
    for v, weight in g.graph[u]:
        G.add_edge(u, v, weight=weight)

pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, node_color='green', node_size=500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)}, label_pos=0.5)

plt.show()