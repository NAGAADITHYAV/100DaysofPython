import matplotlib.pyplot as plt
import networkx as nx

class Node:
    def __init__(self, value, left = None, right = None, balance_factor = 0):
        self.value = value
        self.left = left
        self.right = right
        self.balance_factor = balance_factor

class AvlTree:
    def __init__(self, root = None):
        self.root = root

    def insert(self, node):
        if not self.root:
            self.root = node
            return
        if self.root.val <= node.val:
            
        

    def _print_tree(self, name):
        G = nx.DiGraph()
        # add edges of a tree ot the graph

        #decide positions of the nodes 
        #plot the figure 
        #save the graphs with proper naming convensions so that it can be re seen to decide w


def print_tree():
    G = nx.DiGraph()
    

    # Define parent-child relationships
    edges = [("Root", "A"), ("Root", "B"), ("A", "A1"), ("A", "A2"), ("B", "B1")]
    G.add_edges_from(edges)

    # Define a simple hierarchical layout manually
    pos = {
        "Root": (0, 0),
        "A": (-1, -1), "B": (1, -1),
        "A1": (-1.5, -2), "A2": (-0.5, -2),
        "B1": (1, -2)
    }

    plt.figure(figsize=(6, 4))
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_weight="bold", arrows=True)
    plt.show()

print_tree()