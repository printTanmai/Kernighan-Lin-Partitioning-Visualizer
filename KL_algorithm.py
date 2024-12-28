import sys
import numpy as np
import random
import networkx as nx
import matplotlib.pyplot as plt
from tkinter import Tk, Button, Frame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Define nodes and edges
nodes = [1, 2, 3, 4, 5, 6, 7, 8]  # Enter the nodes here
edges = [(1, 2, 1), (1, 5, 1), (1, 6, 1), (2, 5, 1), (2, 6, 1), (3, 6, 1), 
         (3, 7, 1), (3, 8, 1), (3, 4, 1), (4, 7, 1), (4, 8, 1)]  # The edges are shown as (node1, node2, weight)

# Number of vertices
n = len(nodes)

# Adjacency matrix initialized to zero
A = np.zeros((n + 1, n + 1))  # Create an adjacency matrix with an extra row/column for 1-based indexing

# Create adjacency matrix from the edges
for edge in edges:
    x, y, weight = edge
    A[x, y] = weight
    A[y, x] = weight  # since the graph is undirected

# List of vertices (adjusted to 0-based indexing for convenience in Python)
v = list(range(1, n + 1))

# Divide nodes into two random groups
random.shuffle(v)
cut = int(n / 2)
n1, n2 = np.sort(v[:cut]), np.sort(v[cut:])
pairs = len(n1) * len(n2)

def cut_size(n1, n2):
    """Calculate the cut size (number of edges between nodes in two groups)."""
    r_old = 0
    for i in n1:
        for j in n2:
            if A[i, j] > 0:
                r_old += A[i, j]  # sum of edge weights
    return r_old

def best_swap(n1, n2):
    """Find the best swap between groups to minimize cut size."""
    mark = []
    partition = []
    cut_s = []
    while len(mark) != pairs - 1:
        r_best, ij, part = [], [], []
        r_old = cut_size(n1, n2)
        for i in range(len(n1)):
            for j in range(len(n2)):
                if ([n1[i], n2[j]] not in mark and [n2[j], n1[i]] not in mark):
                    n11, n22 = n1.copy(), n2.copy()
                    n11[i] = n2[j]
                    n22[j] = n1[i]
                    del_R = r_old - cut_size(n11, n22)  # Change in cut size
                    r_best.append(del_R)
                    part.append([n11, n22])
                    ij.append([n11[i], n22[j]])
        
        a = np.argmax(r_best)
        c_part = part[a]
        partition.append(c_part)
        mark.append(ij[a])
        cut_s.append(cut_size(c_part[0], c_part[1]))
        n1, n2 = c_part[0], c_part[1]
    return cut_s[np.argmin(cut_s)], partition[np.argmin(cut_s)]

def kernighan_lin(n1, n2):
    """Perform Kernighan-Lin partitioning to minimize cut size."""
    cs = []
    for _ in range(1):  # Number of iterations
        CutSize, partition = best_swap(n1, n2)
        n1, n2 = partition[0], partition[1]
        cs.append(CutSize)
        # Check if cut size is converging
        if len(cs) >= 10:
            ts = cs[-5:]
            if ts[0] == ts[1] == ts[2] == ts[3] == ts[4]:
                break
    return CutSize, partition

# Perform Kernighan-Lin partitioning
c, p = kernighan_lin(n1, n2)
p1, p2 = np.sort(p[0]), np.sort(p[1])

# Define groups
grp1 = p[0]
grp2 = p[1]

# Create a NetworkX graph
G = nx.Graph()

# Add edges to the graph (using the provided edges)
for edge in edges:
    G.add_edge(edge[0], edge[1], weight=edge[2])

# Tkinter App to visualize the graph
class GraphVisualizationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Graph Partition Visualization")

        # Create a frame to hold the canvas
        self.frame = Frame(root)
        self.frame.pack()

        # Create a button to update the graph
        self.update_button = Button(self.frame, text="Show Partitioned Graph", command=self.update_graph)
        self.update_button.pack()

        # Create a canvas for the matplotlib plot
        self.canvas_frame = Frame(root)
        self.canvas_frame.pack()

    def update_graph(self):
        """Update the graph visualization based on partitions."""
        # Create a matplotlib figure
        fig, ax = plt.subplots(figsize=(8, 6))

        # Get positions for each node (simple circular layout for demo purposes)
        pos = nx.spring_layout(G)  # This can be customized

        # Draw the nodes
        node_colors = ['b' if node in grp1 else 'g' for node in G.nodes()]
        nx.draw(G, pos, ax=ax, node_color=node_colors, with_labels=True, node_size=500, font_size=15, font_weight='bold')

        # Draw edges with weights
        edge_weights = [G[u][v]['weight'] for u, v in G.edges()]
        nx.draw_networkx_edge_labels(G, pos, ax=ax, edge_labels={(u, v): G[u][v]['weight'] for u, v in G.edges()})

        # Embed the plot into the tkinter window
        self.canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

# Create the Tkinter window and run the application
if __name__ == '__main__':
    root = Tk()
    app = GraphVisualizationApp(root)
    root.mainloop()
